from PIL import Image
import numpy as np
from scipy.ndimage import uniform_filter


def spatial_average(image_path, window_sizes):
    image = Image.open(image_path).convert('L')
    img_np = np.array(image)

    results = {}
    for size in window_sizes:
        averaged = uniform_filter(img_np, size=size)
        output_name = f'../output/spatial_average/spatial_avg_{size}x{size}.png'
        Image.fromarray(averaged.astype(np.uint8)).save(output_name)
        results[size] = averaged

    return results


spatial_results = spatial_average('../input/girl.jpg', [3, 10, 20])
