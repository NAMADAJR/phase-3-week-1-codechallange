# Adds two numbers together
def add_number (num1 , num2):
    print (num1 + num2)
add_number(5 , 5)

# Checks if a number is even
def is_even (number):
    print (number % 2 == 0) 
is_even(2)

# Reverses the order of a string
def reverse_string(text):
    print (text[::-1])
reverse_string("maN")

# Count the number of vowels in a word
def count_vowels (text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
       if char in vowels:
           count += 1
    print(f"Number of vowels: {count}")
count_vowels("Mangoes")

# Rerutns the factorial of the number 
def calculate_factorial(n):
    if n < 0:
        print("Enter a non-negative number")
        return None
    factorial = 1
    for i in range (2, n+1):
        factorial *=i
    print (f"Factotial of {n} = {factorial}")
calculate_factorial(5)

# 
def apply_decorator(func):
    def decorator_func(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return decorator_func

@apply_decorator
def sample_function():
    print("Original Function Called")

sample_function()

# Sorts people by age in ascending order
def sort_by_age(people):
    return sorted(people, key=lambda person: person[1])
people = [("Nam", 30), ("Juju", 20), ("Ben", 45), ("Bob", 15)]
sorted_people = sort_by_age(people)
print(sorted_people)

# Mergers two dictionaries
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value 
        else:
            merged_dict[key] = value  
    return merged_dict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

merged = merge_dicts(dict1, dict2)
print(merged)

# DIsplays car info
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"This is a {self.make} {self.model} series, model {self.year}")
my_car = Car("Mercedes", "SLK-200", 2016)
my_car.display_info()