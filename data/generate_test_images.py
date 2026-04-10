"""Generate placeholder test images for Activity 8."""
try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Pillow not installed. Run: pip install Pillow")
    exit(1)

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

IMAGES = {
    "pothole_01.jpg": (640, 480, (100, 100, 100)),      # gray
    "inspection_photo.jpg": (640, 480, (80, 120, 80)),   # dark green
    "graffiti_02.jpg": (640, 480, (180, 50, 50)),        # red
    "streetlight_03.jpg": (640, 480, (200, 200, 50)),    # yellow
    "trash_04.jpg": (640, 480, (80, 60, 40)),            # brown
}


def main():
    for filename, (w, h, color) in IMAGES.items():
        path = os.path.join(SCRIPT_DIR, filename)
        if os.path.exists(path):
            print(f"  [skip] {filename} already exists")
            continue
        img = Image.new("RGB", (w, h), color)
        draw = ImageDraw.Draw(img)
        label = os.path.splitext(filename)[0].replace("_", " ").upper()
        draw.text((10, 10), f"TEST: {label}", fill=(255, 255, 255))
        img.save(path, "JPEG")
        print(f"  [created] {filename}")


if __name__ == "__main__":
    main()
