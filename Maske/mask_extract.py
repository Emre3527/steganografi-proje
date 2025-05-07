from PIL import Image
import numpy as np
import cv2

def mask_extract(stego_image_path):
    img = Image.open(stego_image_path).convert('L')
    data = np.array(img)

    # Kenar tespiti (aynı şekilde yapılmalı)
    sobel = cv2.Sobel(data, cv2.CV_64F, 1, 1, ksize=3)
    edge_mask = np.abs(sobel) > 50

    bits = ''
    h, w = data.shape

    for y in range(h):
        for x in range(w):
            if edge_mask[y, x]:
                bit = data[y, x] & 1
                bits += str(bit)

                if bits.endswith('1111111111111110'):
                    bits = bits[:-16]
                    chars = [bits[i:i+8] for i in range(0, len(bits), 8)]
                    message = ''.join([chr(int(c, 2)) for c in chars])
                    print("Çıkarılan mesaj:", message)
                    return

if __name__ == "__main__":
    mask_extract("penguin_extract.png")