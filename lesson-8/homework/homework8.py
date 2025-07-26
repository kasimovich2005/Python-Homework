# 1.  ZeroDivisionErrorRaqamni nolga bo'lishda istisnolarni hal qilish uchun Python dasturini yozing .



try:
    a = int(input("Son kiriting: "))
    b = int(input("Bo'luvchini kiriting: "))
    result = a / b
    print("Natija:", result)
except ZeroDivisionError:
    print("Xatolik: Nolga bo'lish mumkin emas!")


#  2.  Foydalanuvchini butun sonni kiritishni taklif qiladigan va ValueErroragar kiritilgan butun son bo'lmasa, istisno keltiradigan Python dasturini yozing.

try:
    number = int(input("Butun son kiriting: "))
    print("Kiritilgan son:", number)
except ValueError:
    print("Xatolik: Bu butun son emas.")


#  3. Faylni ochadigan va FileNotFoundErroragar fayl mavjud bo'lmasa, istisnolarni boshqaradigan Python dasturini yozing.


try:
    with open("test.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")



# 4.  Python dasturini yozing, u foydalanuvchidan ikkita raqamni kiritishni taklif qiladi va TypeErroragar kirishlar sonli bo'lmasa, istisno qiladi.

try:
    x = float(input("Birinchi sonni kiriting: "))
    y = float(input("Ikkinchi sonni kiriting: "))
    print("Natija:", x + y)
except ValueError:
    raise TypeError("Faqat raqam kiriting!")



# 5 . PermissionErrorAgar ruxsat bilan bog'liq muammo bo'lsa, faylni ochadigan va istisnolarni boshqaradigan Python dasturini yozing .

try:
    with open("/root/secret.txt", "r") as file:
        print(file.read())
except PermissionError:
    print("Xatolik: Ruxsat yo‘q.")

# 6.  Ro'yxatda amalni bajaradigan va IndexErrorindeks diapazondan tashqarida bo'lsa, istisnolarni bajaradigan Python dasturini yozing.

my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Xatolik: Indeks mavjud emas.")

# 7.  Foydalanuvchiga raqam kiritishni taklif qiladigan va KeyboardInterruptagar foydalanuvchi kiritishni bekor qilsa, istisnoni hal qiladigan Python dasturini yozing.
try:
    num = input("Son kiriting (Ctrl+C bosmang): ")
    print("Siz kiritgan:", num)
except KeyboardInterrupt:
    print("\nXatolik: Foydalanuvchi kiritishni bekor qildi.")


# 8.  ArithmeticErrorAgar arifmetik xato bo'lsa, bo'linishni bajaradigan va istisnolarni bajaradigan Python dasturini yozing .
try:
    a = 10
    b = 0
    c = a / b
except ArithmeticError as e:
    print("Arifmetik xatolik:", e)


# 9.  UnicodeDecodeErrorAgar kodlash muammosi bo'lsa, faylni ochadigan va istisnolarni hal qiladigan Python dasturini yozing .
try:
    with open("example.txt", encoding="ascii") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Xatolik: Unicode kodlashda muammo.")


# 10. Ro'yxat amalini bajaradigan va AttributeErroragar atribut mavjud bo'lmasa, istisnolarni boshqaradigan Python dasturini yozing.



try:
    x = 10
    x.append(5)
except AttributeError:
    print("Xatolik: Bu obyektda bunday metod mavjud emas.")



"""""    Fayl kiritish/chiqarish mashqlari      """


# 1. Butun matn faylini o'qish uchun Python dasturini yozing.
with open("file.txt", "r") as f:
    print(f.read())

# 2. nFaylning birinchi qatorlarini o'qish uchun Python dasturini yozing .
n = 3
with open("file.txt", "r") as f:
    for i in range(n):
        print(f.readline(), end="")

# 3. Faylga matn qo'shish va matnni ko'rsatish uchun Python dasturini yozing.
with open("file.txt", "a") as f:
    f.write("\nYangi qator.")
with open("file.txt", "r") as f:
    print(f.read())

# 4. nFaylning oxirgi satrlarini o'qish uchun Python dasturini yozing .
n = 2
with open("file.txt", "r") as f:
    lines = f.readlines()
    for line in lines[-n:]:
        print(line, end="")

# 5. Faylni satr bo'yicha o'qish va uni ro'yxatga saqlash uchun Python dasturini yozing.
with open("file.txt", "r") as f:
    lines = [line.strip() for line in f]
print(lines)

# 6. Faylni satr bo'yicha o'qish va uni o'zgaruvchiga saqlash uchun Python dasturini yozing.
with open("file.txt", "r") as f:
    data = f.read()
print(data)

# 7. Faylni satr bo'yicha o'qish va uni massivda saqlash uchun Python dasturini yozing.

import array
with open("file.txt", "r") as f:
    arr = array.array('u', f.read())
print(arr)


# 8. Eng uzun so'zlarni topish uchun Python dasturini yozing.

with open("file.txt", "r") as f:
    words = f.read().split()
    max_len = max(len(word) for word in words)
    longest = [word for word in words if len(word) == max_len]
print(longest)


# 9. Matn faylidagi qatorlar sonini hisoblash uchun Python dasturini yozing.

with open("file.txt", "r") as f:
    print("Qatorlar soni:", len(f.readlines()))


# 10. Fayldagi so'zlarning chastotasini hisoblash uchun Python dasturini yozing.


from collections import Counter
with open("file.txt", "r") as f:
    words = f.read().replace(",", " ").split()
    freq = Counter(words)
print(freq)


# 11. Oddiy faylning fayl hajmini olish uchun Python dasturini yozing.

import os
print("Fayl hajmi:", os.path.getsize("file.txt"), "bayt")


# 12. Faylga ro'yxat yozish uchun Python dasturini yozing.

my_list = ["Apple", "Banana", "Cherry"]
with open("fruits.txt", "w") as f:
    for item in my_list:
        f.write(item + "\n")


# 13. Fayl mazmunini boshqa faylga nusxalash uchun Python dasturini yozing.


with open("file.txt", "r") as f1, open("copy.txt", "w") as f2:
    f2.write(f1.read())


# 14. Birinchi fayldagi har bir satrni ikkinchi fayldagi tegishli qator bilan birlashtirish uchun Python dasturini yozing.

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    for l1, l2 in zip(f1, f2):
        print(l1.strip() + " " + l2.strip())


# 15. Fayldan tasodifiy qatorni o'qish uchun Python dasturini yozing.


import random
with open("file.txt", "r") as f:
    lines = f.readlines()
    print(random.choice(lines).strip())


# 16. Fayl yopilgan yoki yopilmaganligini baholash uchun Python dasturini yozing.

f = open("file.txt", "r")
print("Yopilganmi?", f.closed)
f.close()
print("Yopilganmi?", f.closed)


# 17. Fayldan yangi qator belgilarini olib tashlash uchun Python dasturini yozing.


with open("file.txt", "r") as f:
    lines = [line.strip() for line in f]
print(lines)


# 18. Matn faylini kirish sifatida qabul qiladigan va berilgan matn faylidagi so'zlar sonini qaytaradigan Python dasturini yozing.


with open("file.txt", "r") as f:
    text = f.read().replace(",", " ")
    words = text.split()
    print("So‘zlar soni:", len(words))

# 19. Turli matnli fayllardan belgilar ajratib olish va ularni ro'yxatga qo'yish uchun Python dasturini yozing.



import os
chars = []
for filename in os.listdir():
    if filename.endswith(".txt"):
        with open(filename, "r") as f:
            chars.extend(list(f.read()))
print(chars)

# 20. A.txt, B.txtva hokazo nomli 26 ta matnli fayllarni yaratish uchun Python dasturini yozing Z.txt.


import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"Bu {letter}.txt fayli")

# 21. Ingliz alifbosining barcha harflari har bir satrda ma'lum miqdordagi harflar bilan ro'yxatga olingan fayl yaratish uchun Python dasturini yozing.


import string

n = 5  # Har qatorga nechta harf yozish
letters = string.ascii_uppercase

with open("alphabet.txt", "w") as f:
    for i in range(0, len(letters), n):
        f.write("".join(letters[i:i+n]) + "\n")
