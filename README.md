# Talaba Boshqaruv Tizimi (Student Management System)

Bu loyiha, **o'rganish va o'rgatish** maqsadida yaratilgan Django ilovasidir. Talabalar ma'lumotlarini boshqarish uchun asosiy tizim funksiyalarini o'rganishga yordam beradi. Ushbu tizim yordamida talaba ma'lumotlarini saqlash, yangilash, o'chirish va ko'rish mumkin.

## Xususiyatlar

- Talabalar ro'yxatini ko'rish
- Yangi talaba qo'shish
- Talabani tahrirlash
- Talabani o'chirish
- Django admin paneli orqali boshqarish

## Texnologiyalar

- Python 3.x
- Django 4.x
- SQLite (ma'lumotlar bazasi)
- HTML, CSS (foydalanuvchi interfeysi)

## Talablar

- Python 3.x
- Django 4.x
- pip (Python paketlarini boshqarish uchun)

## Loyihani o'rnatish

1. Git repozitoriyasini klonlash:

   ```bash
   git clone https://github.com/whdev36/talaba-boshqaruv-tizimi.git
   ```

2. Virtual muhit yaratish va aktivlashtirish (ixtiyoriy, tavsiya etiladi):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```

3. Loyihadagi barcha kutubxonalarni o'rnatish:

   ```bash
   pip install -r requirements.txt
   ```

4. Ma'lumotlar bazasini yaratish:

   ```bash
   python manage.py migrate
   ```

5. Ishga tushirish:

   ```bash
   python manage.py runserver
   ```

6. Brauzer orqali `http://127.0.0.1:8000` manziliga o'tib, tizimni ishlatishni boshlang.

## Django Admin Paneli

Django admin paneliga kirish uchun quyidagi ma'lumotlar bilan login qiling:

- Foydalanuvchi: `katta_aka`
- Parol: `Admin1234a+`

Admin panel orqali talabalar ro'yxatini boshqarishingiz mumkin.

## Katta Yordam

Agar sizda biron bir savol yoki muammo bo'lsa, quyidagi manzil orqali bog'lanishingiz mumkin:

- Email: [wisdomhunter36.com](mailto:wisdomhunter36.com)

## Lisensiya

Loyiha MIT litsenziyasiga ega. To'liq ma'lumotlar uchun `LICENSE` faylini ko'rib chiqing.
