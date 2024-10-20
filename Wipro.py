"""
1. data types in python 

int, float, complex
list, tuple, range
str
set, frozenset
dict
bool
byte, bytearray, memoryview
None

2. multi threading in python 
3. decorators 
4. generators

Django

1. By default file structure 
2. Create a model employee 
3. List all employees query 
employees = Employee.objects.all()
4. Query to get/create employee with id =5


# Fetch or create the employee with id=5
employee, created = Employee.objects.get_or_create(
    id=5,
    defaults={
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'johndoe@example.com',
        'phone_number': '1234567890',
        'department': 'IT',
        'hire_date': '2024-01-01',
        'salary': 60000,
        'is_active': True
    }
)

if created:
    print(f"Employee with id=5 was created: {employee.first_name} {employee.last_name}")
else:
    print(f"Employee with id=5 already exists: {employee.first_name} {employee.last_name}")


"""
#multi-threading

import threading


def print_cube(num):
    print("Cube: {}" .format(num * num * num))


def print_square(num):
    print("Square: {}" .format(num * num))


if __name__ =="__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")
# DECORATORS
 modify the behaviour of a function or class
# Python program to illustrate functions 
# can be passed as arguments to other functions 
def shout(text): 
    return text.upper() 

def whisper(text): 
    return text.lower() 

def greet(func): 
    # storing the function in a variable 
    greeting = func("""Hi, I am created by a function passed as an argument.""") 
    print (greeting) 

greet(shout) 
greet(whisper) 

#GENERATOR

#its a normal function returns iterator using Yield keyowrd, which later can be used using for loop / next() method


# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1            
    yield 2            
    yield 3            
 
# Driver code to check above generator function
for value in simpleGeneratorFun(): 
    print(value)

o/p: 
1
2
3

# A Python program to demonstrate use of 
# generator object with next() 

# A generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
 
# x is a generator object
x = simpleGeneratorFun()

# Iterating over the generator object using next

# In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))
-----------------------------------------------------------------------------------------

Django
Create a model employee

from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    department = models.CharField(max_length=100)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
