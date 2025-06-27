# code/task2_region_growing.py
import numpy as np
from PIL import Image
import os
from collections import deque


def region_grow(image_array, seed, threshold=10):
    h, w = image_array.shape
    visited = np.zeros((h, w), dtype=bool)
    result = np.zeros((h, w), dtype=np.uint8)

    seed_value = image_array[seed]
    queue = deque([seed])
    visited[seed] = True

    while queue:
        x, y = queue.popleft()
        result[x, y] = 255

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and not visited[nx, ny]:
                    if abs(int(image_array[nx, ny]) - int(seed_value)) <= threshold:
                        queue.append((nx, ny))
                        visited[nx, ny] = True

    return result


def task2(image_path):
    image = Image.open(image_path).convert('L')
    img_np = np.array(image)

    seed = (30, 30)
    region = region_grow(img_np, seed, threshold=20)

    os.makedirs("../output", exist_ok=True)
    Image.fromarray(region).save("../output/region_growing_result.png")


task2("../input/input_image.png")
