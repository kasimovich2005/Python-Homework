# 1. is_prime(n) funksiyasi


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(4))  
print(is_prime(7))  



#  Vazifa 2: digit_sum(k) funksiyasi

def digit_sum(k):
    return sum(map(int, str(k)))

print(digit_sum(24))   
print(digit_sum(502))  


#  Vazifa 3: print_powers_of_two(N) funksiyasi

def print_powers_of_two(N):
    result = []
    power = 1
    while (2 ** power) <= N:
        result.append(2 ** power)
        power += 1
    print(*result)

print_powers_of_two(10)  

