from PIL import Image
import numpy as np

def message_to_binary(message):
    return ''.join(f'{ord(c):08b}' for c in message) + '11111110'  # bitiş işareti

def binary_to_message(binary):
    chars = []
    for i in range(0, len(binary) - 8, 8):
        byte = binary[i:i+8]
        chars.append(chr(int(byte, 2)))
    return ''.join(chars)

def complexity(block):
    """Bit düzeyindeki 8x8 bloğun karmaşıklığını hesapla"""
    return np.sum(block[:, :-1] != block[:, 1:]) + np.sum(block[:-1, :] != block[1:, :])

def embed_message_bpcs(image_path, output_path, message):
    img = Image.open(image_path).convert("L")  # grayscale
    data = np.array(img)
    height, width = data.shape

    bits = message_to_binary(message)
    bit_idx = 0
    bit_planes = np.unpackbits(data.reshape(-1, 1), axis=1).reshape(height, width, 8)

    for k in range(7, -1, -1):  # 8 bit-plane
        for i in range(0, height, 8):
            for j in range(0, width, 8):
                if i+8 > height or j+8 > width:
                    continue
                block = bit_planes[i:i+8, j:j+8, k]
                if complexity(block) > 20:  # karmaşıklığı yüksekse gizle
                    if bit_idx + 64 > len(bits):
                        continue
                    bit_block = np.array([int(b) for b in bits[bit_idx:bit_idx+64]]).reshape(8,8)
                    bit_planes[i:i+8, j:j+8, k] = bit_block
                    bit_idx += 64
                if bit_idx >= len(bits):
                    break
            if bit_idx >= len(bits):
                break
        if bit_idx >= len(bits):
            break

    if bit_idx < len(bits):
        print("⚠️ Mesajın tamamı gömülemedi. Daha büyük resim gerek.")
    else:
        print("✅ Mesaj başarıyla gömüldü.")

    flat = np.packbits(bit_planes.reshape(-1, 8), axis=1).reshape(height, width)
    out_img = Image.fromarray(flat.astype(np.uint8))
    out_img.save(output_path)

def extract_message_bpcs(stego_path):
    img = Image.open(stego_path).convert("L")
    data = np.array(img)
    height, width = data.shape

    bit_planes = np.unpackbits(data.reshape(-1, 1), axis=1).reshape(height, width, 8)
    bits = []

    for k in range(7, -1, -1):  # her bit düzeyi
        for i in range(0, height, 8):
            for j in range(0, width, 8):
                if i+8 > height or j+8 > width:
                    continue
                block = bit_planes[i:i+8, j:j+8, k]
                if complexity(block) > 20:
                    block_bits = block.flatten().tolist()
                    bits.extend([str(b) for b in block_bits])
                    if ''.join(bits[-8:]) == '11111110':
                        message = binary_to_message(bits)
                        print(f"\n🕵️‍♂️ Çözülmüş Mesaj:\n{message}")
                        return
    print("❌ Mesaj bulunamadı.")

def main():
    print("=== BPCS Görsel Steganografi Aracı ===")
    print("1. Mesaj Gömmek")
    print("2. Mesaj Çıkarmak")
    choice = input("Seçiminizi girin (1/2): ")

    if choice == "1":
        image_path = input("Görsel dosya yolu (örnek: input.png): ")
        output_path = input("Çıkış dosyası adı (örnek: stego.png): ")
        message = input("Gömülecek mesajı girin (en fazla 160 karakter): ")
        if len(message) > 160:
            print("⚠️ Mesaj 160 karakterden uzun olamaz.")
            return
        embed_message_bpcs(image_path, output_path, message)

    elif choice == "2":
        stego_path = input("Mesaj içeren görsel dosya (örnek: stego.png): ")
        extract_message_bpcs(stego_path)

    else:
        print("❌ Geçersiz seçim.")

if __name__ == "__main__":
    main()
