#1. Ro‘yxat elementlarini yaratish va ularga kirish


fruits = ["apple", "banana", "cherry", "orange", "grape"]
print(fruits[3])  



# 2. Ikki ro‘yxatni birlashtiring
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  


# 3. Ro‘yxatdan elementlarni ajratib oling
numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]
extracted = [first, middle, last]
print(extracted)  


#4. Ro'yxatni Tuplega o'zgartiring
movies = ["Inception", "Avatar", "Titanic", "The Matrix", "Interstellar"]
movies_tuple = tuple(movies)
print(movies_tuple)


# 5. Ro'yxatdagi elementni tekshiring
cities = ["London", "New York", "Tokyo", "Paris", "Berlin"]
print("Paris" in cities)  



# 6. Looplardan foydalanmasdan ro'yxatni ko'paytirish
nums = [1, 2, 3]
duplicated = nums * 2
print(duplicated) 


# 7. Ro‘yxatning birinchi va oxirgi elementlarini almashtiring
data = [10, 20, 30, 40, 50]
data[0], data[-1] = data[-1], data[0]
print(data) 


# 8. Tupleni kesib oling
numbers_tuple = tuple(range(1, 11))
print(numbers_tuple[3:8])  



# 9. Ro‘yxatdagi hodisalarni sanash
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
count_blue = colors.count("blue")
print(count_blue)  


# 10. Tupledagi element indeksini toping
animals = ("cat", "dog", "lion", "tiger", "elephant")
index_lion = animals.index("lion")
print(index_lion)  # Output: 2



# 11. Ikki kortejni birlashtiring
t1 = (1, 2, 3)
t2 = (4, 5, 6)
merged = t1 + t2
print(merged)  # Output: (1, 2, 3, 4, 5, 6)


# 12. Ro‘yxat va to‘plam uzunligini toping
my_list = [1, 2, 3, 4]
my_tuple = (5, 6, 7)
print(len(my_list))  # Output: 4
print(len(my_tuple))  # Output: 3


# 13. Tupleni ro'yxatga aylantiring

numbers = (10, 20, 30, 40, 50)
numbers_list = list(numbers)
print(numbers_list)

# 14. Tupledagi maksimal va minimal qiymatlarni toping
values = (100, 200, 50, 75, 300)
print(max(values))  # Output: 300
print(min(values))  # Output: 50


# 15. Tupleni teskari o'zgartirish

words = ("hello", "world", "python", "rocks")
reversed_tuple = words[::-1]
print(reversed_tuple)  # Output: ('rocks', 'python', 'world', 'hello')










