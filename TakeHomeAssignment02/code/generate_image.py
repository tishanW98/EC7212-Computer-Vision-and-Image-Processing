from PIL import Image, ImageDraw
import os


def generate_synthetic_image(save_path):
    img = Image.new('L', (300, 300), color=200)
    draw = ImageDraw.Draw(img)

    draw.rectangle([50, 50, 150, 150], fill=80)

    draw.ellipse([160, 160, 280, 280], fill=40)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    img.save(save_path)
    print(f"Smooth synthetic image saved to {save_path}")


generate_synthetic_image("../input/synthetic_image.png")
