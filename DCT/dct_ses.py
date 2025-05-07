def embed_text_in_image(image_path, message, output_path):
    if len(message) > 160:
        print("⚠️ Mesaj 160 karakterden uzun olamaz.")
        return

    with open(image_path, 'rb') as img_file:
        img_data = img_file.read()

    marker = b'STEGTEXT'
    message_bytes = message.encode('utf-8')
    combined_data = img_data + marker + message_bytes

    with open(output_path, 'wb') as out_file:
        out_file.write(combined_data)

    print(f"✅ Mesaj başarıyla '{output_path}' dosyasına gömüldü.")

def extract_text_from_image(stego_image_path):
    with open(stego_image_path, 'rb') as file:
        data = file.read()

    marker = b'STEGTEXT'
    idx = data.find(marker)
    if idx == -1:
        print("❌ Mesaj bulunamadı.")
        return

    hidden_message = data[idx + len(marker):].decode('utf-8', errors='ignore')
    print(f"🕵️‍♂️ Çözülmüş Mesaj:\n{hidden_message}")

def main():
    print("=== Görsele Metin Gömme ve Çözme Aracı ===")
    print("1. Metin Göm")
    print("2. Metni Çöz")
    choice = input("Seçiminizi girin (1/2): ")

    if choice == "1":
        img = input("Görsel dosya yolu (örnek: image.png): ")
        message = input("Gömülecek mesajı girin (maks. 160 karakter): ")
        out = input("Çıkış görsel dosya adı (örnek: output.png): ")
        embed_text_in_image(img, message, out)

    elif choice == "2":
        stego = input("Mesaj içeren görsel dosya (örnek: output.png): ")
        extract_text_from_image(stego)

    else:
        print("❌ Geçersiz seçim.")

if __name__ == "__main__":
    main()
