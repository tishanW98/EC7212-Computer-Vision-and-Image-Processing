from PIL import Image
import numpy as np

def block_average(image_path, block_sizes):
    image = Image.open(image_path).convert('L')
    img_np = np.array(image)

    results = {}
    for block_size in block_sizes:
        h, w = img_np.shape
        h_trim = h - (h % block_size)
        w_trim = w - (w % block_size)

        trimmed = img_np[:h_trim, :w_trim]
        reshaped = trimmed.reshape(
            h_trim // block_size, block_size, w_trim // block_size, block_size)
        averaged_blocks = reshaped.mean(axis=(1, 3)).astype(np.uint8)

        expanded = np.repeat(
            np.repeat(averaged_blocks, block_size, axis=0), block_size, axis=1)
        Image.fromarray(expanded).save(
            f'../output/4_block_average/block_avg_{block_size}x{block_size}.png')
        results[block_size] = expanded

    return results

block_avg_results = block_average('../input/girl.jpg', [3, 5, 7])
