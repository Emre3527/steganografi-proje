from PIL import Image
import numpy as np
import cv2

def message_to_bits(message):
    bits = ''.join([format(ord(c), '08b') for c in message])
    bits += '1111111111111110'
    return list(bits)

def mask_embed(image_path, output_path, message):
    img = Image.open(image_path).convert('L')
    data = np.array(img)

    sobel = cv2.Sobel(data, cv2.CV_64F, 1, 1, ksize=3)
    edge_mask = np.abs(sobel) > 50  # Kenar eşiği

    bits = message_to_bits(message)
    bit_index = 0

    h, w = data.shape

    for y in range(h):
        for x in range(w):
            if edge_mask[y, x] and bit_index < len(bits):
                pixel = data[y, x]
                pixel = (pixel & 0b11111110) | int(bits[bit_index])  # LSB ile değiştir
                data[y, x] = pixel
                bit_index += 1

    result = Image.fromarray(data.astype(np.uint8))
    result.save(output_path)
    print("Mesaj başarıyla kenar bölgelerine gömüldü:", output_path)

if __name__ == "__main__":
    msg = input("Gömülecek mesaj (max 160 karakter): ")
    mask_embed("penguin.png", "penguin_extract.png", msg)