from PIL import Image


def rotate_image(image_path, angles):
    image = Image.open(image_path)
    for angle in angles:
        rotated = image.rotate(angle, expand=True)
        rotated.save(f'../output/3_rotation/rotated_{angle}.png')


rotate_image('../input/girl.jpg', [45, 90])
