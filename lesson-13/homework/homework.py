# Age Calculator

from datetime import datetime

tugilgan_kun = input("Tug‘ilgan kuningizni kiriting (YYYY-MM-DD): ")
tugilgan_sana = datetime.strptime(tugilgan_kun, "%Y-%m-%d")
bugun = datetime.today()

yil = bugun.year - tugilgan_sana.year
oy = bugun.month - tugilgan_sana.month
kun = bugun.day - tugilgan_sana.day

if kun < 0:
    oy -= 1
    kun += 30

if oy < 0:
    yil -= 1
    oy += 12

print(f"Siz {yil} yil, {oy} oy, {kun} kunliksiz.")





# 2. Days Until Next Birthday


from datetime import datetime, timedelta

birthdate_str = input("Tu'gulgan yil-oy-sana ingizni kiritng (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
today = datetime.today()
next_birthday = birthdate.replace(year=today.year)

if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_left = (next_birthday - today).days
print(f"{days_left} kundan keyin sizning tug'ulgan kuningiz")



#3. Meeting Scheduler


from datetime import datetime, timedelta

sana_str = input("Hozirgi sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
soat = int(input("Uchrashuv davomiyligi (soat): "))
minut = int(input("Uchrashuv davomiyligi (minut): "))

boshlanish_vaqti = datetime.strptime(sana_str, "%Y-%m-%d %H:%M")
tugash_vaqti = boshlanish_vaqti + timedelta(hours=soat, minutes=minut)

print("Uchrashuv tugaydigan vaqt:", tugash_vaqti.strftime("%Y-%m-%d %H:%M"))



# 4.Timezone Converter

from datetime import datetime
import pytz

jordan = input("Hozirgi vaqt zonangizni kiriting (masalan: Asia/Tashkent): ")
boshqa = input("O‘zgartirmoqchi bo‘lgan vaqt zonasi (masalan: Europe/London): ")
vaqt_str = input("Sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")

asosiy_vaqt = datetime.strptime(vaqt_str, "%Y-%m-%d %H:%M")
asosiy_zona = pytz.timezone(jordan)
yangi_zona = pytz.timezone(boshqa)

asosiy_vaqt = asosiy_zona.localize(asosiy_vaqt)
yangi_vaqt = asosiy_vaqt.astimezone(yangi_zona)

print("O‘zgartirilgan vaqt:", yangi_vaqt.strftime("%Y-%m-%d %H:%M %Z%z"))




# 5. Orqaga Sanovchi Taymer
from datetime import datetime
import time

kelajak_str = input("Kelajakdagi vaqtni kiriting (YYYY-MM-DD HH:MM:SS): ")
kelajak = datetime.strptime(kelajak_str, "%Y-%m-%d %H:%M:%S")

while True:
    hozir = datetime.now()
    if hozir >= kelajak:
        print("⏰ Vaqt tugadi!")
        break
    qolgan = kelajak - hozir
    print("Qolgan vaqt:", qolgan, end="\r")
    time.sleep(1)

#6. Email Tekshiruvchi

import re

email = input("Email manzilini kiriting: ")
namuna = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(namuna, email):
    print("Email manzili to‘g‘ri.")
else:
    print("Email manzili noto‘g‘ri.")


# 7. Telefon Raqamini Formatlash

raqam = input("10 xonali telefon raqamingizni kiriting (faqat raqamlar): ")

if len(raqam) == 10 and raqam.isdigit():
    formatlangan = f"({raqam[:3]}) {raqam[3:6]}-{raqam[6:]}"
    print("Formatlangan raqam:", formatlangan)
else:
    print("Telefon raqami noto‘g‘ri.")



#8. Parol Kuchini Tekshiruvchi

import re

parol = input("Parol kiriting: ")

if (len(parol) >= 8 and
    re.search(r'[A-Z]', parol) and
    re.search(r'[a-z]', parol) and
    re.search(r'[0-9]', parol)):
    print("Kuchli parol.")
else:
    print("Parol kuchsiz. Kamida 8 belgi, katta, kichik harf va raqam bo‘lishi kerak.")




# 9. Matndan So‘z Qidiruvchi

import re

matn = """Bu oddiy matn. Bu yerda 'top' so‘zini topamiz. Topish juda foydali."""
soz = input("Qidiriladigan so‘zni kiriting: ")

natija = re.findall(soz, matn, re.IGNORECASE)
print(f"'{soz}' so‘zi {len(natija)} marta topildi.")



#  10. Matndan Sana Ajratish


import re

matn = input("Matn kiriting (masalan: 2025-08-06 yoki 06/08/2025): ")

namuna = r'\b(?:\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})\b'
sanalari = re.findall(namuna, matn)

if sanalari:
    print("Topilgan sanalar:")
    for sana in sanalari:
        print("-", sana)
else:
    print("Sana topilmadi.")





