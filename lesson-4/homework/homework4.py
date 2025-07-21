"""""   1. Sort a Dictionary by Value    """


my_dict = {'apple': 10, 'banana': 5, 'cherry': 7}

asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", asc_sorted)

desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", desc_sorted)



"""""   2. Add a Key to a Dictionary    """

d = {0: 10, 1: 20}

d[2] = 30
print(d)



"""""   3. Concatenate Multiple Dictionaries   """


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = {}
for d in (dic1, dic2, dic3):
    result.update(d)
print(result)

result = {**dic1, **dic2, **dic3}
print(result)


"""""  4. Generate a Dictionary with Squares  """


n = 5
squares = {x: x**2 for x in range(1, n+1)}
print(squares)


""" 5. Dictionary of Squares (1 to 15) """


squares_15 = {x: x**2 for x in range(1, 16)}
print(squares_15)


#  Set Exercises

"""1. Create a Set"""

my_set = {1, 2, 3, 4, 5}
print(my_set)


""" 2. Iterate Over a Set """

my_set = {"apple", "banana", "cherry"}
for item in my_set:
    print(item)



""" 3. Add Member(s) to a Set """

my_set = {1, 2, 3}
my_set.add(4)             
my_set.update([5, 6, 7])    
print(my_set)




""""" 4. Remove Item from Set"""

my_set = {1, 2, 3, 4, 5}
my_set.remove(3)  # Removes 3; raises error if not present
print(my_set)

# Or use discard (no error if not found)
my_set.discard(10)
print(my_set)


""""" 5. Remove ab Item if Present in the Set"""

my_set = {10, 20, 30, 40}
if 20 in my_set:
    my_set.remove(20)
print(my_set)










