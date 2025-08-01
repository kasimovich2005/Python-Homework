# exercise 1

import threading

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    for num in range(start, end):
        if is_prime(num):
            result.append(num)

def threaded_prime_checker(start, end, num_threads):
    threads = []
    results = [[] for _ in range(num_threads)]
    step = (end - start) // num_threads

    for i in range(num_threads):
        s = start + i * step
        e = end if i == num_threads - 1 else s + step
        t = threading.Thread(target=check_primes, args=(s, e, results[i]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    all_primes = []
    for r in results:
        all_primes.extend(r)
    
    print("Prime numbers:", sorted(all_primes))


threaded_prime_checker(1, 100, 4)


# exercise 2

import threading
from collections import Counter

def process_lines(lines, counter_list, index):
    local_counter = Counter()
    for line in lines:
        words = line.strip().lower().split()
        local_counter.update(words)
    counter_list[index] = local_counter

def threaded_word_count(file_path, num_threads=4):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    chunk_size = total_lines // num_threads
    threads = []
    counters = [None] * num_threads

    for i in range(num_threads):
        start = i * chunk_size
        end = total_lines if i == num_threads - 1 else (i + 1) * chunk_size
        t = threading.Thread(target=process_lines, args=(lines[start:end], counters, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total_counter = Counter()
    for c in counters:
        total_counter.update(c)

    for word, count in total_counter.most_common():
        print(f"{word}: {count}")


