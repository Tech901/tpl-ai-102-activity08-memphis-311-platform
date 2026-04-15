"""Visible tests for Activity 8 - Memphis 311 AI Platform."""
import json
import os
import re

import pytest

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
RESULT_PATH = os.path.join(BASE_DIR, "result.json")
DESIGN_PATH = os.path.join(BASE_DIR, "design.json")
EVAL_PATH = os.path.join(BASE_DIR, "eval_report.json")
MAIN_PATH = os.path.join(BASE_DIR, "app", "main.py")


@pytest.fixture
def result():
    if not os.path.exists(RESULT_PATH):
        pytest.skip("result.json not found - run 'python app/main.py' first")
    with open(RESULT_PATH) as f:
        return json.load(f)


@pytest.fixture
def design():
    if not os.path.exists(DESIGN_PATH):
        pytest.skip("design.json not found - run 'python app/main.py' first")
    with open(DESIGN_PATH) as f:
        return json.load(f)


@pytest.fixture
def eval_report():
    if not os.path.exists(EVAL_PATH):
        pytest.skip(
            "eval_report.json not found - run 'python app/main.py' first"
        )
    with open(EVAL_PATH) as f:
        return json.load(f)


def test_result_exists():
    """Canary: result.json must exist."""
    assert os.path.exists(RESULT_PATH), (
        "Run 'python app/main.py' to generate result.json"
    )


def test_design_exists():
    """design.json must exist."""
    assert os.path.exists(DESIGN_PATH), (
        "Run 'python app/main.py' to generate design.json"
    )


def test_eval_report_exists():
    """eval_report.json must exist."""
    assert os.path.exists(EVAL_PATH), (
        "Run 'python app/main.py' to generate eval_report.json"
    )


def test_required_fields(result):
    for field in ("task", "status", "outputs", "metadata"):
        assert field in result, f"Missing required field: {field}"


def test_task_name(result):
    assert result["task"] == "memphis_311_platform"


def test_status_valid(result):
    assert result["status"] in ("success", "partial", "error")


def test_outputs_has_text_intake(result):
    text = result["outputs"].get("text_intake", {})
    assert isinstance(text, dict) and text.get("routed_to"), (
        "text_intake missing or not routed -- implement Step 1"
    )


def test_outputs_has_photo_intake(result):
    photo = result["outputs"].get("photo_intake", {})
    assert isinstance(photo, dict) and photo.get("routed_to"), (
        "photo_intake missing or not routed -- implement Step 2"
    )


def test_outputs_has_question_intake(result):
    question = result["outputs"].get("question_intake", {})
    assert isinstance(question, dict) and question.get("routed_to"), (
        "question_intake missing or not routed -- implement Step 3"
    )


def test_outputs_has_agent_routing(result):
    routing = result["outputs"].get("agent_routing", {})
    has_any = any(
        routing.get(k) for k in
        ("text_routed_to", "photo_routed_to", "question_routed_to")
    )
    assert has_any, (
        "agent_routing has no routed pipelines -- implement Steps 1-4"
    )


def test_safety_blocks_injection(result):
    """Malicious input must be flagged as unsafe by actual safety logic."""
    safety = result["outputs"].get("safety_results", {})
    malicious = safety.get("malicious", {})
    assert malicious.get("safe") is False, (
        "Malicious prompt injection was not blocked -- implement Step 5"
    )
    assert "error" not in malicious, (
        "Safety check raised an error instead of running -- "
        "implement check_injection() in Step 5"
    )


def test_design_has_rationale(design):
    """design.json must include a non-empty architecture rationale."""
    rationale = design.get("architecture", {}).get("rationale", "")
    assert isinstance(rationale, str) and len(rationale.strip()) > 0, (
        "design.json architecture.rationale must be non-empty"
    )


def test_telemetry_present(result):
    """result.json metadata must include telemetry data."""
    telemetry = result.get("metadata", {}).get("telemetry", {})
    assert isinstance(telemetry, dict) and len(telemetry) > 0, (
        "metadata.telemetry is missing or empty -- implement Step 6"
    )


def test_no_hardcoded_keys():
    with open(MAIN_PATH) as f:
        source = f.read()
    suspicious = [
        r'["\']https?://\S+\.cognitiveservices\.azure\.com\S*["\']',
        r'["\'][A-Fa-f0-9]{32}["\']',
    ]
    for pattern in suspicious:
        matches = re.findall(pattern, source)
        real = [
            m for m in matches
            if "example" not in m.lower() and "your-" not in m.lower()
        ]
        assert len(real) == 0, (
            f"Possible hardcoded credential: {real[0][:50]}"
        )
