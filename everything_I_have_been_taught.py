print(51+38)
print(20+16)
print(60+10)
print(5+70)
print(89+72)

name = "Onaademipo"
print(name)

age = "7"
print(age)

i_love_my_family = True
print(i_love_my_family)

favourite_movie = "Sonic the Hedgehog"
print(favourite_movie)

favourite_colour = "Black"
print(favourite_colour)

favourite_subject = "maths"
print(favourite_subject)

favourite_food = "Noodles"
print(favourite_food)

least_favourite_food = "Oat"
print(least_favourite_food)

birth_month = "July"
print(birth_month)

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
    count = 1
while count <= 5:
    print(count)
    count += 1  # Incrementing the count variable
    #Looping through a list of animals
animals = ["dog", "cat", "rabbit", "hamster"]
for animal in animals:
    print("I have a", animal)
user_input = ""
while user_input != "quit":
    user_input = input("Enter a word (type 'quit' to exit): ")
    print("You entered:", user_input)
# Looping through a dictionary of ages
ages = {"Dara": 11, "Nola": 9, "Naade": 7}
for name, age in ages.items():
    print(name, "is", age, "years old")

favourite_fruit = ["apple"]

if favourite_fruit != favourite_fruit:
    print("My hated fruits are", favourite_fruit)
else:
    print("My favourite fruits are", favourite_fruit)

sentence = input("sentence:")
words = sentence.split()
for word in words:
    print(f"{word}: len{word}")

numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
total = 0
for num in numbers:
    total += num

    print("Sum of numbers:", total)

import random

random_number = random.randint(1, 40)
guess = 0

while guess != random_number:
    guess = int(input("Guess the number(between 1 and 40): "))
    if guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")

password = "Meowmix"

while True:
    user_input = input("password: ")
    if user_input == password:
        print("Correct. Welcome Ms Souza!")
        break
    else:
        print("No hackers! If you are one!")
    
countdown_number = int(input("Enter countdown munber please:"))

while countdown_number > 0:
    print(countdown_number)
    countdown_number -=1
print("fly!")

x= 16
y= 15

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")

num1 = 12
num2 = 200

if num1 > num2:
    print("num1 is greater than num2")
else:
    print("num1 is not greater than num2")

age = 19

if age != 19:
    print("You are not 19 years old")
else:
    print("You are 19 years old")

temperature = 1

if temperature < 30:
    print("it is a cool day")
else:
    print("it is not a cool day")

James = 20
Mary = 30

if James > Mary:
    print("James has more apples")
else:
    print("|Mary has more apples")

Tom = 10
Anna = 15

if Tom == Anna:
    print("Tom and Anna are the same age")
else:
    print("Tom and Anna have dirrerent ages")

Emily = 24

if Emily < 80:
    print("Emily's score is less than 80")
else:
    print("Emily's score is 80 or higher")

David = 125

if David >= 150:
    print("David is tall enough")
else:
    print("David is not tall enough")

lily = tuple

if lily == tuple:
    print("lily's favourite colour is green")
else:
    print("lily's favourite colour is not green")

a = 300
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

    score = 553
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

    ages = {"Adejoke": 9, "Nola": 9, "Dara": 11, "Teacher": 25}
print("Dictionary of ages:", ages)

#Example 1: Dictionary of ages:
ages = {"Dara": 11, "Nola": 9, "Naade": 7}
print("Dictionary of ages", ages)

#Example 2:Dictionary of book titles and their authors
books = {"Python Crash Course": "Eric Matthes", "Deep Learning": "Ian Goodfellow"}
print("Dictionary of books", books)

# Example 3: Dictionary of superhero powers
superheroes = {"Superman": "Flying", "Batman": "Gadgets", "Wonder Woman": "Lasso of Truth"}
print("Dictionary of superheroes:", superheroes)

#Example 4: Accessing elements in a dictionary
Daras_age = ages["Dara"] # Accessing Dara's age: 11
print("Dara's age:", Daras_age)

book_author = books["Python Crash Course"] # Accessing the author of the book "Python Crash Course"
print("Author of Python Crash Course:", book_author)

#Example 5: Modifying dictionaries
ages["Dara"] = 14 # Updating Dara's age to 14
print("Updating ages:", ages)

books["Deep Learning"] = "Yoshua Bengio" # Correcting the author of the book "Deep Learning"
print("Updated books:", books)

superheroes["Batman"] = "Utility Belt" # Updating Batman's power
print("Updated superheroes:", superheroes)

age = 25
if age < 5:
    print("free")
elif age >= 5 and age <= 12:
    print("$10 child ticket")
elif age >= 65:
    print("$12 senior ticket")
else:
    print("$20 regular ticket")

    username = "user"
password = "secret"
if username == "admin" and password == "admin123":
    print("Admin access granted")
elif username == "user123" and password == "secret123":
    print("User access granted")
else:
    print("Access denied")

    import datetime
hour = datetime.datetime.now().hour
if hour < 12:
    print("Good Morning")
elif hour < 17:
    print("Good Afternoon")
else:
    print("Good Evening")

    temperature = -1
if temperature < 0:
    print("Freezing")
elif temperature >= 0 and temperature < 10:
    print("Cold")
elif temperature >= 10 and temperature < 25:
    print("Moderate")
else:
    print("Warm")

    print("You are in a magical land with three doors")
door = input("Which door will you choose(1, 2, 3, 4)?")
if door == "1":
    print("You found a hidden treasure! Congratulations!")
elif door == "2":
    print("A friendly dragon appears and offers you a wish. What do you wish for?")
    wish = input("I wish for:")
    print(f"You wished for {wish}. The dragon grants your wish!")
elif door == "3":
    print("Oops! You fell into a pit, but a helpful squirrel rescues you.")
elif door == "4":
    print("A zombie wishes to marry you. yes or no?")
    yes = "You lived a long live"
    no = "You died but a girl revived you."
else:
    print("Invalid choice. Please choose a door(1, 2, 3, 4).")

# Define a function called greet()
def greet():
    print("Hello, everyone!")

# Calling the function
greet()  # This will print "Hello, everyone!"

def greet_person(name):
    print("Hello,", name)

greet_person("David")

def square(number):
    return number * number

num = square(55)
print(num)

def number(num5):
    return num5 + 100
num5 = 500
print(num5 + 100)

def greet():
    print("Welcome to Python everyone!")

greet()

def add_numbers(num5, num7):
   return num5 + num7

num5 = 500
num7 = 500
print(add_numbers(1200, 5000))

def multiply_by_two(num6):
    return num6 * 2

num6 = 5000000
print(multiply_by_two(111111133333333))

def combine_strings(str1, str2):
    return str1 + " " + str2

str1 = "Hello"
str2 = "World"

result = combine_strings(str1, str2)
print(result)

def convert_into_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

result = convert_into_celsius(68)
print(result)

def caculate_statistics(number):

    count = len(number)

    total = sum(number)

    mean = total / count if count > 0 else 0

    sorted_number = sorted(number)

    if count % 2 == 0:
        
        median = (sorted_number[count // 2 - 1] + sorted_number[count // 2] / 2)
    else:
        median = sorted_number[count // 2]
    
    minimum = min(number) if count > 0 else 0
    maximum = max(number) if count > 0 else 0
    
    print("Total count:", count)
    print("Sum:", total)
    print("Mean (Average)", mean)
    print("Median:", median)
    print("Minimum", minimum)
    print("Maximum", maximum)

number_list = [7, 12, 5, 21, 8, 10, 15]
caculate_statistics(number_list)

def describe_person(name, color):
    print(f"My name is", name, "My fav color is", color)

name = "Nola"
color = "Rainbow"

result = describe_person(name, color)

def multiplication_table(number):
    table = ""
    i = 1
    while i <= 15:
        result = number * i
        table += f"{number} x {i} = {result}\n"
        i += 1
    return table

number = 8
result = multiplication_table(number)
print(f"Multiplication table for{number}:\n{result}")

def remove_even_numbers(input_list):
    i = 0
    while i < len(input_list):
        if input_list[i] % 2 == 0:
            input_list.pop(i)
        else:
            i += 1
    return input_list
        
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = remove_even_numbers(numbers)
print("List without even numbers:", result)