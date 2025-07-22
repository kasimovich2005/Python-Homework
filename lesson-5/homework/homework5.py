#  1. is_leap(year) Function

def is_leap(year):
    
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


#  2. Conditional Statements Exercise

n = int(input("Enter a number: "))

if n % 2 == 1:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else: 
    print("Not Weird")



# 3. Find Even Numbers Between a and b Without Loop

a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a > b:
    a, b = b, a

if a % 2 != 0:
    a += 1

even_numbers = list(range(a, b+1, 2))
print(even_numbers)



 # Solution 2: Using filter() and lambda (No if-else)

a = int(input("Enter a: "))
b = int(input("Enter b: "))

# Get sorted range and filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, range(min(a, b), max(a, b)+1)))
print(even_numbers)
