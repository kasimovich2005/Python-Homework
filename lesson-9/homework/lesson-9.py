# 1. Circle Class


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())


# 2. Person Class


from datetime import datetime

class Person:
    def __init__(self, name, country, dob):  # dob format: 'YYYY-MM-DD'
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, '%Y-%m-%d')

    def age(self):
        today = datetime.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

# Example
p = Person("Ali", "Uzbekistan", "2000-05-15")
print("Age:", p.age())


# 3. Calculator Class



class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b): return a / b if b != 0 else "Division by zero!"

calc = Calculator()
print(calc.add(5, 3))
print(calc.divide(10, 0))


# 4. Shape and Subclasses


import math

class Shape:
    def area(self): pass
    def perimeter(self): pass

class Circle(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return math.pi * self.radius**2
    def perimeter(self): return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c): self.a, self.b, self.c = a, b, c
    def perimeter(self): return self.a + self.b + self.c
    def area(self):  # Heron's formula
        s = self.perimeter() / 2
        return (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side ** 2
    def perimeter(self): return 4 * self.side


s = Square(4)
print("Square area:", s.area())


# 5. Binary Search Tree Class

class Node:
    def __init__(self, value): self.value, self.left, self.right = value, None, None

class BST:
    def __init__(self): self.root = None

    def insert(self, value):
        def _insert(node, value):
            if not node: return Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node
        self.root = _insert(self.root, value)

    def search(self, value):
        def _search(node, value):
            if not node: return False
            if value == node.value: return True
            return _search(node.left, value) if value < node.value else _search(node.right, value)
        return _search(self.root, value)

tree = BST()
tree.insert(10)
tree.insert(5)
tree.insert(20)
print(tree.search(5))   
print(tree.search(100)) 


# 6. Stack Data Structure

class Stack:
    def __init__(self): self.stack = []

    def push(self, item): self.stack.append(item)
    def pop(self): return self.stack.pop() if self.stack else "Stack is empty"

s = Stack()
s.push(10)
s.push(20)
print(s.pop()) 


# 7. Linked List Data Structure

class Node:
    def __init__(self, data): self.data, self.next = data, None

class LinkedList:
    def __init__(self): self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev, temp = temp, temp.next
        if temp: prev.next = temp.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.display()
ll.delete(1)
ll.display()


# 8. Shopping Cart Class


class ShoppingCart:
    def __init__(self): self.cart = {}

    def add_item(self, name, price):
        self.cart[name] = self.cart.get(name, 0) + price

    def remove_item(self, name):
        if name in self.cart: del self.cart[name]

    def total(self): return sum(self.cart.values())

cart = ShoppingCart()
cart.add_item("apple", 1.5)
cart.add_item("milk", 2.0)
print("Total:", cart.total())
cart.remove_item("milk")
print("Total after removal:", cart.total())



# 9. Stack with Display


class Stack:
    def __init__(self): self.items = []

    def push(self, item): self.items.append(item)
    def pop(self): return self.items.pop() if self.items else "Empty"
    def display(self): print(self.items)

s = Stack()
s.push(10)
s.push(20)
s.display()
s.pop()
s.display()


# 10. Queue Data Structure


class Queue:
    def __init__(self): self.items = []

    def enqueue(self, item): self.items.append(item)
    def dequeue(self): return self.items.pop(0) if self.items else "Empty"

q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  


# 11. Bank Class

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount): self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
    def display(self):
        print(f"{self.name}'s balance: {self.balance}")

acc = BankAccount("Ali", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.display()

