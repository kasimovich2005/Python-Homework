#1. Modify String with Underscores


my_txt = 'abcabcabcdeabcdefabcdefgyt'

used_chars = ['a', 'e', 'i', 'o', 'u']

index = 2

while index < len(my_txt)-1 :
    if my_txt[index] not in used_chars:
         my_txt = my_txt[:index+1] + '_' + my_txt[index+1:]
         used_chars.append(my_txt[index])
         index += 4
    else:
        index += 1
        
print(my_txt)


#2. Integer Squares Exercise

n = int(input())
for i in range(n):
    print(i**2)


# 3. Loop-Based Exercises
# Exercise 1:

i = 1
while i <= 10:
    print(i)
    i += 1


# Exercise 2:


for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()



#Exercise 3:

n = int(input("Enter number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum is:", total)


# Exercise 4:


n = int(input("Enter number: "))
for i in range(1, 11):
    print(n * i)

# Exercise 5:


numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    if num % 5 == 0 and num <= 150:
        print(num)

# Exercise 6:


num = int(input("Enter a number: "))
count = 0
while num != 0:
    num //= 10
    count += 1
print("Total digits:", count)

# Exercise 7:


for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

# Exercise 8:


list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)

# Exercise 9:


for i in range(-10, 0):
    print(i)

# Exercise 10:


for i in range(5):
    print(i)
else:
    print("Done!")


# Exercise 11:


start = 25
end = 50
print("Prime numbers between 25 and 50:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

# Exercise 12:


a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(10):
    print(a, end='  ')
    a, b = b, a + b

# Exercise 13:


num = int(input("Enter number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"{num}! = {fact}")





#  4. Return Uncommon Elements of Lists


from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []

    for key in (c1.keys() | c2.keys()):
        if c1[key] != c2[key]:
            result.extend([key] * abs(c1[key] - c2[key]))
    return result

# Examples
print(uncommon_elements([1, 1, 2], [2, 3, 4]))            # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))            # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5])) # [2, 2, 5]
