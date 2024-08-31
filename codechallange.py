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

# Count the nimber of vowels in a word
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



