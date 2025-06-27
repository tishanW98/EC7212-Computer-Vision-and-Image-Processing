# code/task1_otsu_thresholding.py
import numpy as np
from PIL import Image
from skimage import filters
import os

def add_gaussian_noise(image_array, mean=0, std=15):
    noise = np.random.normal(mean, std, image_array.shape)
    noisy = np.clip(image_array + noise, 0, 255).astype(np.uint8)
    return noisy

def task1(image_path):
    image = Image.open(image_path).convert('L')
    img_np = np.array(image)

    noisy_img = add_gaussian_noise(img_np)
    threshold = filters.threshold_otsu(noisy_img)
    mask = (noisy_img >= threshold).astype(np.uint8) * 255

    os.makedirs("../output", exist_ok=True)
    Image.fromarray(noisy_img).save("../output/noisy_image.png")
    Image.fromarray(mask.astype(np.uint8)).save("../output/otsu_mask.png")
    
    print(f"Otsu Threshold Value: {threshold}")

task1("../input/synthetic_image.png")
