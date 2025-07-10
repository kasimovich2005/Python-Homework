#  Python Homework 2 

# 1 - Exercises  = Age Calculator

name = input("Ismingizni kiriting: ")
birtday = int(input("Tug'ulgan yilingizni Kiriting: "))
hozirgi_sana = 2025



yosh = hozirgi_sana - birtday

print(name , f"Sizning yoshingiz: {yosh} yosh")





# 2 - Exercises  = Extract Car Names


txt = 'LMaasleitbtui'
car_name = txt[::2]  
print(car_name) 


# 3 - Exercises  = Extract Car Names


txt2 = 'MsaatmiazD'
car2 = txt2[1::2]
print("Extracted Car Name 2:", car2) 





# 4 - Exercises = Extract Residence Area


txt = "I'am John. I am from London"
residence = txt[21:]  # 21-indeksdan oxirigacha olamiz
print("Residence Area:", residence)


# 5 -  Exercises = Reverse String


gap = input("Teskarisiga foydalanmoqchi  bo'gan so'z: ")
teskari_gap = gap[::-1]
print("Teskari matn:", teskari_gap)


# 6-  Exercises = Count Vowels


text = input("Matn kiriting: ")
count = 0

for harf in text:
    if harf in "aeiouAEIOU":
        count += 1

print("Unli harflar soni:", count)



# 7. Find Maximum Value


numbers = input("Raqamlarni probel bilan kiriting: ").split()
numbers = [int(n) for n in numbers]
max_value = max(numbers)
print("Eng katta qiymat:", max_value)



# 8. Check Palindrome
word = input("So'z kiriting: ")
if word == word[::-1]:
    print("Bu so'z palindrome.")
else:
    print("Bu so'z palindrome emas.")



# 9. Extract Email Domain

email = input("Email kiriting: ")
domain = email.split("@")[1]
print("Domen:", domain)



#  10. Generate Random Password

import random
import string

uzunligi = 12  # Parol uzunligi
char = string.ascii_letters + string.digits + string.punctuation
parol = ''.join(random.choice(char) for _ in range(uzunligi))
print("Tasodifiy parol:", parol)

