def add_number (num1 , num2):
    print (num1 + num2)
add_number(5 , 5)

def is_even (number):
    print (number % 2 == 0) 
is_even(2)

def reverse_string(text):
    print (text[::-1])
reverse_string("maN")

def count_vowels (text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
       if char in vowels:
           count += 1
    print(f"Number of vowels: {count}")
count_vowels("Mangoes")

