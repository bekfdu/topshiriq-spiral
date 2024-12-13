# Spiral matritsa topshirig'i

Ushbu loyiha `7x7` o‘lchamdagi spiral matritsa yaratib, uni 1 dan `49` gacha bo‘lgan sonlar bilan to‘ldiradi va vizualizatsiya qiladi. Matritsa rangli xarita ko‘rinishida tasvirlanadi va ustiga matritsa elementlari yozib qo‘yiladi.
![image](https://github.com/user-attachments/assets/ab034aad-efc0-43cc-b9e0-c163a90b5d2e)


## Xususiyatlari

- Berilgan `7` qiymati asosida spiral matritsa yaratadi.
- Matritsani `Matplotlib` yordamida rangli ko‘rinishda vizualizatsiya qiladi.
- Matritsa elementlari aniq ko‘rinishi uchun ustiga sonlar yoziladi.

## Dasturning Ishlash Tizimi

1. **`spiral_matrix(n)` funksiyasi**:
   - Matritsa yuqori chap burchakdan boshlab spiral tarzda sonlar bilan to‘ldiriladi.
   - Yo‘nalish avtomatik ravishda o‘zgarib, sonlar chegaradan tashqariga chiqib ketmasligi ta’minlanadi.
2. Natijada hosil bo‘lgan matritsa `Matplotlib` yordamida tasvirlanadi:
   - Rangli xarita (color map) yordamida matritsa aks ettiriladi.
   - Matritsa elementlari ustiga raqamlar qo‘shiladi.

## Talablar

Dasturni ishlatish uchun quyidagi kutubxonalar o‘rnatilgan bo‘lishi kerak:

- Python 3.7 yoki undan yuqori versiyasi
- `matplotlib` (vizualizatsiya uchun)
- `numpy` (matritsa yaratish uchun)

Kutubxonalarni o‘rnatish uchun quyidagi buyruqdan foydalanishingiz mumkin:

```
pip install matplotlib numpy
```
Dasturni Ishga Tushirish
Repositoriyani klonlang:

```
git clone https://github.com/bekfdu/topshiri-spiral.git
```
Loyihaga kirib oling:

```
cd spiral-matrix-visualization
```
Skriptni ishga tushiring:

```
python spiral_matrix.py
```
Matritsaning vizualizatsiyasi Matplotlib oynasida aks etadi.

Misol Natija
n = 7 uchun spiral matritsa quyidagicha ko‘rinishga ega:

```
1  2  3  4  5  6  7
24 25 26 27 28 29 8
23 40 41 42 43 30 9
22 39 48 49 44 31 10
21 38 47 46 45 32 11
20 37 36 35 34 33 12
19 18 17 16 15 14 13
```
Vizualizatsiyada matritsa rangli xaritada, sonlar ustiga yozilgan holda aks ettiriladi.



Loyiha haqida
Ushbu loyiha Python dasturlash tili va uning asosiy kutubxonalari yordamida bajarilgan va dasturlash bo‘yicha o‘z ko‘nikmalarimni namoyish etish uchun yaratilgan.
