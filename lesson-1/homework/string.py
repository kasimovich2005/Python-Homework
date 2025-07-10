#  Homework1 

# 1. Given a side of square. Find its perimeter and area.

N=int(input("Kvadrat tomonini kiriting: "))
Area=N*N
Perimeter=4*N
print(Area)
print(Perimeter)



#2. Given diameter of circle. Find its length.


import math
diameter = float(input("Doiraning diametrini kiriting: "))
length = math.pi * diameter
print(length)




#3 Given two numbers a and b. Find their mean.




a = float(input("a sonini kiriting: "))
b = float(input("b sonini kiriting: "))

# O'rtacha qiymatni hisoblash
avg = (a + b) / 2

# Natijani chiqarish
print(f"O'rtacha qiymat: {avg:.2f}")





#  4. Given two numbers a and b. Find their sum, product and square of each number.



a = float(input("a sonini kiriting: "))
b = float(input("b sonini kiriting: "))

# Yig'indisi
sum_result = a + b

# Ko‘paytmasi
product_result = a * b

# Kvadrati
square_a = a ** 2
square_b = b ** 2

# Natijalarni chiqarish
print(f"Yig'indisi: {sum_result}")
print(f"Ko‘paytmasi: {product_result}")
print(f"a sonining kvadrati: {square_a}")
print(f"b sonining kvadrati: {square_b}")





