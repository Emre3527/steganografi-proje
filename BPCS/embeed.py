from PIL import Image
import numpy as np

def complexity(block):
    flat = block.flatten()
    transitions = np.sum(flat[:-1] != flat[1:])
    return transitions / (len(flat) - 1)

def message_to_bits(message):
    bits = ''.join([format(ord(c), '08b') for c in message])
    bits += '1111111111111110'
    return list(bits)

def bpcs_embed(image_path, output_path, message):
    img = Image.open(image_path).convert("L")
    data = np.array(img)

    h, w = data.shape
    block_size = 8
    message_bits = message_to_bits(message)
    bit_index = 0

    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            if bit_index >= len(message_bits):
                break

            block = data[y:y+block_size, x:x+block_size]
            if block.shape != (8, 8):
                continue

            for bit_plane in range(1, 8):
                plane = ((block >> bit_plane) & 1).astype(np.uint8)
                if complexity(plane) > 0.3:
                    for i in range(8):
                        for j in range(8):
                            if bit_index < len(message_bits):
                                plane[i, j] = int(message_bits[bit_index])
                                bit_index += 1

                    mask = 255 ^ (1 << bit_plane)
                    block = block & mask
                    block = block | (plane.astype(np.uint8) << bit_plane)


            data[y:y+block_size, x:x+block_size] = block

    result = Image.fromarray(data.astype(np.uint8))
    result.save(output_path)
    print("Mesaj başarıyla gömüldü:", output_path)

if __name__ == "__main__":
    msg = input("Mesaj (max 160 karakter): ")
    bpcs_embed("penguin.png", "penguin1.png", msg)