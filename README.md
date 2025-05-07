
# 📦 LSB Steganografi

## 📌 Açıklama (Description)
LSB (Least Significant Bit) yöntemi ile görüntü, ses ve video verilerine gizli mesaj gömme ve çıkarma işlemleri yapılır.

---

## 🧰 Gereksinimler (Requirements)
- Python 3.8+
- numpy, opencv-python
- argparse
- Diğer: Ses dosyalarında genellikle .wav, videolarda .mp4/.avi formatları tercih edilir.

```bash
pip install -r requirements.txt
```

---

## ⚙️ Kurulum (Setup)

```bash
cd LSB
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🚀 Kullanım (Usage)

### 📥 Mesaj Gömme (Embed)

```bash
python lsb_ses.py  # Gerekirse parametrelerle
```

### 📤 Mesaj Çıkarma (Extract)

```bash
python lsb_video_tool.py  
```

---

## 📎 Notlar (Notes)
- Desteklenen medya türleri: image, audio, video
- Ses dosyalarında genellikle .wav, videolarda .mp4/.avi formatları tercih edilir.



# 📦 DCT Steganografi

## 📌 Açıklama (Description)
JPEG DCT (Discrete Cosine Transform) tabanlı steganografi yöntemi ile JPEG formatındaki görüntülere veri gömülür.

---

## 🧰 Gereksinimler (Requirements)
- Python 3.8+
- numpy, opencv-python
- argparse
- Diğer: Yalnızca .jpeg uzantılı görsellerde çalışır. Diğer formatlarda hata verebilir.

```bash
pip install -r requirements.txt
```

---

## ⚙️ Kurulum (Setup)

```bash
cd DCT
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🚀 Kullanım (Usage)

### 📥 Mesaj Gömme (Embed)

```bash
python dct_ses.py  
```

### 📤 Mesaj Çıkarma (Extract)

```bash
python dct_ses.py  
```

---

## 📎 Notlar (Notes)
- Desteklenen medya türleri: image (.jpeg)
- Yalnızca .jpeg uzantılı görsellerde çalışır. Diğer formatlarda hata verebilir.



# 📦 BPCS Steganografi

## 📌 Açıklama (Description)
Bit Plane Complexity Segmentation algoritması ile yüksek karmaşıklık taşıyan bit düzeylerine veri gömülür.

---

## 🧰 Gereksinimler (Requirements)
- Python 3.8+
- numpy, opencv-python
- argparse
- Diğer: 160 karaktere kadar mesaj gömülebilir. Görüntü boyutu mesaj uzunluğuna bağlı olarak değişebilir.

```bash
pip install -r requirements.txt
```

---

## ⚙️ Kurulum (Setup)

```bash
cd BPCS
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🚀 Kullanım (Usage)

### 📥 Mesaj Gömme (Embed)

```bash
python bpcs_message.py  
```

### 📤 Mesaj Çıkarma (Extract)

```bash
python bpcs_message.py  # Gerekirse parametrelerle
```

---

## 📎 Notlar (Notes)
- Desteklenen medya türleri: image
- 160 karaktere kadar mesaj gömülebilir. Görüntü boyutu mesaj uzunluğuna bağlı olarak değişebilir.



# 📦 Maske Steganografi

## 📌 Açıklama (Description)
Görüntüde kenar tespiti (Sobel/Canny) ile maskelenmiş alanlara LSB yöntemiyle mesaj gizleme ve çıkarma işlemleri yapılır.

---

## 🧰 Gereksinimler (Requirements)
- Python 3.8+
- numpy, opencv-python
- argparse
- Diğer: Yüksek kenar içeren görüntülerde daha iyi sonuç verir. LSB sadece kenar bölgelerine uygulanır.

```bash
pip install -r requirements.txt
```

---

## ⚙️ Kurulum (Setup)

```bash
cd Maske
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🚀 Kullanım (Usage)

### 📥 Mesaj Gömme (Embed)

```bash
python mask_embeed.py  
```

### 📤 Mesaj Çıkarma (Extract)

```bash
python mask_extract.py  
```

---

## 📎 Notlar (Notes)
- Desteklenen medya türleri: image, video
- Yüksek kenar içeren görüntülerde daha iyi sonuç verir. LSB sadece kenar bölgelerine uygulanır.



# 📦 Sezgisel Steganografi

## 📌 Açıklama (Description)
LSB içeren görsellerin istatistiksel özelliklerini analiz ederek gizli veri içerip içermediğini tahmin eden makine öğrenmesi modeli.

---

## 🧰 Gereksinimler (Requirements)
- Python 3.8+
- numpy, opencv-python
- scikit-learn, argparse
- Diğer: RandomForestClassifier ile LSB tabanlı steganografi tespiti yapılır. clean/ ve stego/ klasörleri gerekir.

```bash
pip install -r requirements.txt
```

---

## ⚙️ Kurulum (Setup)

```bash
cd Sezgisel
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🚀 Kullanım (Usage)

### 📥 Mesaj Gömme (Embed)

```bash
python detect.py  
```

### 📤 Mesaj Çıkarma (Extract)

```bash
python detect.py  
```

---

## 📎 Notlar (Notes)
- Desteklenen medya türleri: image
- RandomForestClassifier ile LSB tabanlı steganografi tespiti yapılır. clean/ ve stego/ klasörleri gerekir.
