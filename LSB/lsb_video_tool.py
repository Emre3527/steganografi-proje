import cv2
import numpy as np

def message_to_bits(message):
    return ''.join(f'{ord(c):08b}' for c in message) + '11111110'

def bits_to_message(bits):
    chars = []
    for i in range(0, len(bits) - 8, 8):  # -8: sonlandırıcıyı dahil etme
        byte = bits[i:i+8]
        chars.append(chr(int(''.join(byte), 2)))
    return ''.join(chars)

def embed_message_in_video(input_video, output_video, message):
    cap = cv2.VideoCapture(input_video)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    width = int(cap.get(3))
    height = int(cap.get(4))
    fps = cap.get(5)
    out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    bits = message_to_bits(message)
    bit_idx = 0
    written = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if not written:
            flat = frame.flatten()
            for i in range(len(flat)):
                if bit_idx >= len(bits):
                    break
                flat[i] = (flat[i] & 254) | int(bits[bit_idx])
                bit_idx += 1
            frame = flat.reshape(frame.shape)
            written = True

        out.write(frame)

    cap.release()
    out.release()
    print(f"\n✅ Mesaj başarıyla '{output_video}' dosyasına gömüldü.")

def extract_message_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    bits = []
    read = False

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if not read:
            flat = frame.flatten()
            for i in range(len(flat)):
                bits.append(str(flat[i] & 1))
                if ''.join(bits[-8:]) == '11111110':
                    read = True
                    break

        if read:
            break

    cap.release()
    message = bits_to_message(bits)
    print(f"\n🕵️‍♂️ Çözülmüş Mesaj:\n{message}")

def main():
    print("=== LSB Video Steganografi Aracı ===")
    print("1. Mesaj Gömmek (Encode)")
    print("2. Mesaj Çıkarmak (Decode)")
    choice = input("Seçiminizi girin (1/2): ")

    if choice == "1":
        input_video = input("Girdi video dosyası (örnek: input.mp4): ")
        output_video = input("Çıkış video dosyası (örnek: output.avi): ")
        message = input("Gömülecek mesajı girin (max 160 karakter): ")
        if len(message) > 160:
            print("⚠ Mesaj 160 karakterden uzun olamaz.")
            return
        embed_message_in_video(input_video, output_video, message)

    elif choice == "2":
        input_video = input("Mesaj içeren video dosyası (örnek: output.avi): ")
        extract_message_from_video(input_video)

    else:
        print("❌ Geçersiz seçim.")

if __name__ == "__main__":
    main()
