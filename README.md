# Phase 3 weeek 1 Code Challenge

### By Namada Junior

## Project description
My code snippets demonstrate basic functionality in Python. Here's a summary of what each function or class does:

1. Adding Two Numbers: add_number(num1, num2): Adds two numbers and prints the result.
```py
def add_number (num1 , num2):
    print (num1 + num2)
add_number(5 , 5)
```

2. Checking if a Number is Even: is_even(number): Checks if the provided number is even and prints True or False.
```py
def is_even (number):
    print (number % 2 == 0) 
is_even(2)
```

3. Reversing a String: reverse_string(text): Reverses the given string and prints it.
```py
def reverse_string(text):
    print (text[::-1])
reverse_string("maN")
```

4. Counting Vowels in a Word: count_vowels(text): Counts and prints the number of vowels in a given string.
```py
def count_vowels (text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
       if char in vowels:
           count += 1
    print(f"Number of vowels: {count}")
count_vowels("Mangoes")
```

5. Calculating the Factorial of a Number: calculate_factorial(n): Calculates and prints the factorial of a non-negative integer.
```py
def calculate_factorial(n):
    if n < 0:
        print("Enter a non-negative number")
        return None
    factorial = 1
    for i in range (2, n+1):
        factorial *=i
    print (f"Factotial of {n} = {factorial}")
calculate_factorial(5)
```

6. Using a Decorator:
- apply_decorator(func): A simple decorator that prints a message before calling the decorated function.
- sample_function(): A function decorated with apply_decorator, which prints a message before and after its execution.
```py
def apply_decorator(func):
    def decorator_func(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return decorator_func

@apply_decorator
def sample_function():
    print("Original Function Called")

sample_function()
```

7. Sorting People by Age: sort_by_age(people): Sorts a list of tuples (representing people and their ages) by age in ascending order.
```py
def sort_by_age(people):
    return sorted(people, key=lambda person: person[1])
people = [("Nam", 30), ("Juju", 20), ("Ben", 45), ("Bob", 15)]
sorted_people = sort_by_age(people)
print(sorted_people)
```

8. Merging Two Dictionaries: merge_dicts(dict1, dict2): Merges two dictionaries. If the same key exists in both, it adds their values together.
```py
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
```

9. Displaying Car Info:
- Car: A class representing a car with attributes for make, model, and year.
- display_info(): A method that prints a formatted string describing the car.
```py
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"This is a {self.make} {self.model} series, model {self.year}")
my_car = Car("Mercedes", "SLK-200", 2016)
my_car.display_info()
```

## Development

Want to contribute? Excellent!

To enhance or contribute on the existing project, follow these steps:

- Fork the repo
- Create a new branch (git checkout -b enhance-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -m 'enhanced feature')
- Push to the branch (git push origin enhance-feature)
- Create a Pull Request

## License

MIT License

Copyright (c) [2024] [Namada Junior]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.




