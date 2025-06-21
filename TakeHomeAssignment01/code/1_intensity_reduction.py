from PIL import Image
import numpy as np

def reduce_intensity(image_path, levels):
    image = Image.open(image_path).convert('L')  # Grayscale
    img_np = np.array(image)

    step = 256 // levels
    reduced = (img_np // step) * step
    Image.fromarray(reduced.astype(np.uint8)).save(
        f'../output/1_intensity_reduction/intensity_{levels}.png')
    return reduced


reduced_img = reduce_intensity('../input/girl.jpg', 2)
