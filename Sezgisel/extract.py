from PIL import Image
import numpy as np

def heuristic_extract(image_path):
    img = Image.open(image_path).convert("L")
    data = np.array(img)
    h, w = data.shape

    bits = ''
    block_size = 8

    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            block = data[y:y+block_size, x:x+block_size]
            if block.shape != (8, 8):
                continue

            if np.var(block) > 100:
                for i in range(8):
                    for j in range(8):
                        bits += str(block[i, j] & 1)
                        if bits.endswith('1111111111111110'):
                            bits = bits[:-16]
                            chars = [bits[i:i+8] for i in range(0, len(bits), 8)]
                            message = ''.join([chr(int(c, 2)) for c in chars])
                            print("Mesaj:", message)
                            return

if __name__ == "__main__":
    heuristic_extract("penguin_extract.png")