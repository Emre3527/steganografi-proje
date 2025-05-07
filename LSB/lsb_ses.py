import wave

def message_to_bits(message):
    return ''.join(f'{ord(c):08b}' for c in message)

def embed_message(audio_path, output_path, message):
    bits = message_to_bits(message) + '11111110'  # 8-bitlik sonlandırıcı

    song = wave.open(audio_path, mode='rb')
    frames = bytearray(song.readframes(song.getnframes()))
    song_params = song.getparams()
    song.close()

    if len(bits) > len(frames):
        raise ValueError("Mesaj çok uzun, ses dosyası yeterli değil.")

    for i in range(len(bits)):
        frames[i] = (frames[i] & 254) | int(bits[i])

    with wave.open(output_path, 'wb') as modified:
        modified.setparams(song_params)
        modified.writeframes(frames)

    print(f"\n✅ Mesaj başarıyla {output_path} dosyasına gömüldü.")

def extract_message(audio_path):
    song = wave.open(audio_path, mode='rb')
    frames = bytearray(song.readframes(song.getnframes()))
    song.close()

    bits = [str(frames[i] & 1) for i in range(len(frames))]
    chars = []

    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if ''.join(byte) == '11111110':
            break
        chars.append(chr(int(''.join(byte), 2)))

    message = ''.join(chars)
    print(f"\n🕵‍♂ Çözülmüş Mesaj: {message}")

def main():
    print("=== LSB Ses Steganografi Aracı ===")
    print("1. Mesaj Gömmek")
    print("2. Mesaj Çıkarmak")
    choice = input("Seçiminizi girin (1/2): ")

    if choice == "1":
        audio_path = input("Girdi WAV dosyasının adını girin (örnek: orijinal.wav): ")
        output_path = input("Çıkış WAV dosyasının adını girin (örnek: gizli_mesaj.wav): ")
        message = input("Gömülecek mesajı girin (160 karaktere kadar): ")
        if len(message) > 160:
            print("⚠  Mesaj 160 karakterden uzun olamaz.")
            return
        embed_message(audio_path, output_path, message)

    elif choice == "2":
        audio_path = input("Mesaj içeren WAV dosyasının adını girin: ")
        extract_message(audio_path)

    else:
        print("❌ Geçersiz seçim.")

if __name__ == "__main__":
    main()
