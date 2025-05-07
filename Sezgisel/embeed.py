from PIL import Image
import numpy as np

def message_to_bits(message):
    bits = ''.join([format(ord(c), '08b') for c in message])
    bits += '1111111111111110'
    return list(bits)

def heuristic_embed(image_path, output_path, message):
    img = Image.open(image_path).convert("L")
    data = np.array(img)
    h, w = data.shape

    message_bits = message_to_bits(message)
    bit_idx = 0

    block_size = 8
    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            if bit_idx >= len(message_bits):
                break

            block = data[y:y+block_size, x:x+block_size]
            if block.shape != (8, 8):
                continue

            # Sezgisel karar: varyansı yüksekse mesaj göm
            if np.var(block) > 100:
                for i in range(8):
                    for j in range(8):
                        if bit_idx < len(message_bits):
                            pixel = block[i, j]
                            pixel = (pixel & 0b11111110) | int(message_bits[bit_idx])
                            block[i, j] = pixel
                            bit_idx += 1

            data[y:y+block_size, x:x+block_size] = block

    result = Image.fromarray(data.astype(np.uint8))
    result.save(output_path)
    print("Mesaj gömüldü:", output_path)

if __name__ == "__main__":
    msg = input("Mesaj (max 160 karakter): ")
    heuristic_embed("penguin.png", "penguin_extract.png", msg)