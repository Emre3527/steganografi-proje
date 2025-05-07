from PIL import Image
import jpegio as jio
import numpy as np
import os

def convert_png_to_jpg(png_path: str, jpg_path: str):
    img = Image.open(png_path).convert("RGB")
    img.save(jpg_path, "JPEG")
    print(f"✅ PNG dönüştürüldü: {jpg_path}")

def encode_dct(input_path: str, message: str, output_path: str) -> bool:
    try:
        jpg = jio.read(input_path)
        coeffs = jpg.coef_arrays[0]

        message += "###"
        bits = ''.join(format(ord(char), '08b') for char in message)
        bit_index = 0

        h, w = coeffs.shape
        for i in range(0, h, 8):
            for j in range(0, w, 8):
                block = coeffs[i:i+8, j:j+8]
                for x in range(8):
                    for y in range(8):
                        if x == 0 and y == 0:
                            continue
                        if bit_index >= len(bits):
                            break
                        if block[x, y] == 0:
                            continue
                        block[x, y] = (block[x, y] & ~1) | int(bits[bit_index])
                        bit_index += 1
                    if bit_index >= len(bits):
                        break
                if bit_index >= len(bits):
                    break
            if bit_index >= len(bits):
                break

        jio.write(jpg, output_path)
        print(f"✅ Mesaj başarıyla gömüldü: {output_path}")
        return True

    except Exception as e:
        print(f"[DCT encode error] {e}")
        return False

def decode_dct(input_path: str) -> str:
    try:
        jpg = jio.read(input_path)
        coeffs = jpg.coef_arrays[0]

        bits = []
        h, w = coeffs.shape

        for i in range(0, h, 8):
            for j in range(0, w, 8):
                block = coeffs[i:i+8, j:j+8]
                for x in range(8):
                    for y in range(8):
                        if x == 0 and y == 0:
                            continue
                        if block[x, y] == 0:
                            continue
                        bits.append(str(block[x, y] & 1))
                        if len(bits) % 8 == 0:
                            chars = ''.join(chr(int(''.join(bits[k:k+8]), 2)) for k in range(0, len(bits), 8))
                            if chars.endswith("###"):
                                return chars.replace("###", "")
        return ""

    except Exception as e:
        print(f"[DCT decode error] {e}")
        return ""

# 🧪 Örnek kullanım
if __name__ == "__main__":
    png_path = "penguin.png"
    jpg_path = "penguin.jpg"
    stego_path = "stego_penguin.jpg"
    secret_message = "This is a hidden message inside DCT."

    # PNG'yi JPG'ye dönüştür
    if not os.path.exists(jpg_path):
        convert_png_to_jpg(png_path, jpg_path)

    # Mesajı göm
    if encode_dct(jpg_path, secret_message, stego_path):
        # Mesajı çıkar
        revealed = decode_dct(stego_path)
        print("📤 Çıkarılan mesaj:", revealed)
