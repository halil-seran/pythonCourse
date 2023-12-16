# print('lets try again')

# name = ('halil')
# print('hello', name)
# print(type(name))
# first_name = 'halil'
# last_name = 'seran'
# full_name = first_name + ' ' + last_name
# print(full_name)

# age = 25
# age += 1
# print("Your age: " + str(age))

# height = 250.5
# print(type(height))

# isHuman = True
# print(isHuman)

# name, age, isHuman = 'halil', 25, True
# print(name, age, isHuman)

# age1 = age2 = age3 = 25
# print(age1, age2, age3)

# name = 'halil'
#
# print(name)
# print(len(name))
# print(name.find('i'))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count('l'))
# print(name.replace('l', 'm'))
# print(name*3)

# x=1
# y=2.1
# z='3'
#
# x=float(x)
# y=str(y)
# z=int(z)
#
# print(x)
# print(y)
# print(z*3)

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# height = float(input("Enter your height: "))
#
# age += 1
#
# print("Hello " + name)
# print("Your age: " + str(age))
# print("Your height: " + str(height))


# import math
#
# pi=math.pi
#
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi * -1)) #mutlak deger
# print(pow(pi,2)) #ust alma
# print(math.sqrt(pi)) #karekok
#
# x=1
# y=2
# z=3
# print(max(x,y,z))
# print(min(x,y,z))

# name = "halil seran"
#
# first_name = name[:5]
# last_name = name[6:]
# funky_name = name[::2]
# reversed_name = name[: :-1]
#
# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

# website = "http://www.google.com"
#
# slice = slice(11,-4)
#
# print(website[slice])

# age = int(input("Enter your age: "))
#
# if age <= 18:
#     print("You can't drive")
# elif age == 50:
#     print("You are 50")
# elif age > 18 and age < 100:
#     print("You can drive")
# else:
#     print("You forgot to die")

# temp = int(input("Enter the temperature: "))
#
# if not temp < 30:
#     print("It's hot")
# elif temp < 10 and temp > 0:
#     print("It's cold")
# elif temp <= 0:
#     print("It's freezing")
# else:
#     print("It's ok")

# while 1==1:
#     print("im stuck help me")
#     infinite loop

# name = ""
#
# while len(name) == 0:
#     name = input("Enter your name: ")
#
# print("Hello " + name)

# for i in range(10):
#     print(i)®

# for i in range(10,30+1,2):
#     print(i)

# for i in "halil seran":
#     print(i)

# import time
#
# for seconds in range(10,0-1,-1):
#     print(seconds)
#     time.sleep(1)
# print("Happy new year")

# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# symbol = input("Enter a symbol to use: ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phone_number = "123-456-7890"
#
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

# for i in range(1,21):
#     if i == 13 or i == 4:
#         continue
#     print(i)

# food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
#
# food[0] = "sushi"
#
# food.append("ice cream")
# food.remove("hotdog")
# food.pop()
# food.insert(0, "cake")
# food.sort()
# food.clear()


# print(food[0])

# for x in food:
#     print(x)

# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice cream"]
#
# food = [drinks, dinner, dessert]
#
# print(food[1][2])

# student = ("halil", 25, "male")
#
# print(student.count("halil"))
# print(student.index("male"))
#
# for x in student:
#     print(x)
#
# if "halil" in student:
#     print("halil is here")

# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)
# dinner_table = utensils.union(dishes)

# print(utensils.difference(dishes))
# print(utensils.intersection(dishes))

#
# for x in utensils:
#     print(x)

# capitals = {'USA': 'Washington DC',
#             'India': 'New Delhi',
#             'China': 'Beijing',
#             'Russia': 'Moscow'}
#
# print(capitals['India'])
# print(capitals.get('Germany','not found'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
#
# for key, value in capitals.items():
#     print(key, value)
#
# capitals.update({'Germany': 'Berlin'})
# capitals.pop('China')
# capitals.update({'USA': 'Las Vegas'})
# capitals.clear()

# name = "halil seran!"
# if(name[0].islower()):
#     name = name.capitalize()
#
# first_name = name[:5].upper()
# last_name = name[6:11].upper()
# last_character = name[-1]
#
# print(first_name + ' ' + last_name + last_character)

# def hello(first_name, last_name, age):
#     print("hello" + " " + first_name + " " + last_name + " " + str(age))
#
# my_name = "Halil"
# hello(my_name, "Seran", 25)

# def multiply(number1, number2):
#     return number1 * number2
#
# print(multiply(2,3))

# def hello(first, middle, last):
#     print("Hello " + first + " " + middle + " " + last)
#
# hello("Halil", "Seran", "")
# hello(last="Seran", first="Halil", middle="")

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
#
# print(num)
#
# print(round(abs(float(input("Enter a whole positive number: ")))))


# name = "x"
# def display_name():
#     name = "Halil"
#     print(name)
#
# print(name)
# display_name()
#
# #LEGB rule


# def add(*args):
#     sum = 0
#     changeable = list(args)
#     changeable[0] = 5
#     for i in args:
#         sum += i
#     return sum + changeable[0]
#
# print(add(1,2,3,4,5,6,7,8,9,10))

# def hello (**kwargs):
#     print("Hello " + kwargs['first'] + " " + kwargs['last'])
#     print("Hello", end=" ")
#     for key, value in kwargs.items():
#         print(value, end=" ")
#
# hello(title="Mr.", first="Bro",middle="Dude",last="Code")


# animal = "cow"
# item = "moon"
#
# print("The " + animal + " jumped over the " + item)
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(animal, item))
# print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))

# text = "The {} jumped over the {}"
# print(text.format("cow", "moon"))

# name = "Halil"
#
# print("Hello {}".format(name))
# print("Hello {:10}. Nice to meet you".format(name))
# print("Hello {lastname:10}. Nice to meet you".format(lastname="seran"))
# print("Hello {:<10}. Nice to meet you".format(name))
# print("Hello {:>10}. Nice to meet you".format(name))
# print("Hello {:^10}. Nice to meet you".format(name))

# number = 3.14159
# number2 = 1000000
#
# print("The number pi is {:.2f}".format(number))
# print("The number pi is {:,}".format(number2))
# print("The number pi is {:b}".format(number2))
# print("The number pi is {:o}".format(number2))
# print("The number pi is {:x}".format(number2))
# print("The number pi is {:E}".format(number2))

# import random
#
# x = random.randint(1,6)
# y = random.random()
#
# myList = ["rock", "paper", "scissors"]
# z = random.choice(myList)
#
# cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
#
#
# random.shuffle(cards)
# print(cards)
# print(x)
# print(y)
# print(z)

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator /  denominator
# except ZeroDivisionError as e:
#     print(e)
#     print("You can't divide by zero")
# except ValueError as e:
#     print(e)
#     print("Enter only numbers")
# except Exception as e:
#     print(e)
#     print("something went wrong")
# else:
#     print(result)
# finally:
#     print("This will always execute")

# import os
#
# path = "/Users/halil/Desktop/aws.png"
#
# if(os.path.exists(path)):
#     print("That location exists")
#     if(os.path.isfile(path)):
#         print("That is a file")
#     elif(os.path.isdir(path)):
#         print("That is a directory")
# else:
#     print("That location doesn't exist")


# try:
#     with open("test.txt", "w") as file:
#        file.write("Hello\nWorld")
#     with open("test.txt", "a") as file:
#        file.write("Hello\nWorld")
#     with open("test.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("That file was not found")

# copyfile() =copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

# import shutil
#
# shutil.copy("test.txt", "copy-test.txt")

# import os
#
# source = "/Users/halil/PycharmProjects/pythonProject/test.txt"
# destination = "/Users/halil/PycharmProjects/pythonProject/copy-test.txt"
#
# try:
#     if(os.path.exists(destination)):
#         print("There is already a file there")
#     else:
#         os.replace(source, destination)
#         print("File was copied successfully")
# except:
#     print("File was copied successfully")

# import os
#
# path = "copytest.txt"
# os.remove(path)
#
# try:
#     os.remove(path)
# except FileNotFoundError as e:
#     print(e)

# import messages as msg
#
# msg.say_hi()
# msg.say_bye()
#
# from messages import say_hi, say_bye
#
# say_hi()
# say_bye()

# help("modules")

# rock paper scissors game

# import random
#
# computer = random.choice(["rock", "paper", "scissors"])
#
# input("Welcome to rock, paper, scissors. Press enter to start")
#
# player = input("Choose rock, paper or scissors: ").lower().strip()
#
# if player == computer:
#     print("player: " + player)
#     print("computer: " + computer)
#     print("Tie")
# elif player == "rock" and computer == "paper":
#     print("player: " + player)
#     print("computer: " + computer)
#     print("You lose", computer, "covers", player)
# elif player == "rock" and computer == "scissors":
#     print("player: " + player)
#     print("computer: " + computer)
#     print("You win", player, "smashes", computer)
# elif player == "paper" and computer == "rock":
#     print("player: " + player)
#     print("computer: " + computer)
#     print("You win", player, "covers", computer)
# elif player == "paper" and computer == "scissors":
#     print("player: " + player)
#     print("computer: " + computer)
#     print("You lose", computer, "cuts", player)
# elif player == "scissors" and computer == "paper":
#     print("player: " + player)
#     print("computer: " + computer)
#     print("You win", player, "cuts", computer)
# elif player == "scissors" and computer == "rock":
#     print("player: " + player)
#     print("computer: " + computer)
#     print("You lose", computer, "smashes", player)
# else:
#     print("Check your spelling...")

# rock paper scissors game

# import random
#
# while True:
#     choices = ["rock", "paper", "scissors"]
#
#     computer = random.choice(choices)
#     player = None
#
#     while player not in choices:
#         player = input("rock, paper or scissors?: ").lower()
#
#     if player == computer:
#         print("computer: " + computer)
#         print("player: " + player)
#         print("Tie")
#     elif player == "rock":
#         if computer == "paper":
#             print("computer: " + computer)
#             print("player: " + player)
#             print("You lose", computer, "covers", player)
#         if computer == "scissors":
#             print("computer: " + computer)
#             print("player: " + player)
#             print("You win", player, "smashes", computer)
#     elif player == "paper":
#         if computer == "rock":
#             print("computer: " + computer)
#             print("player: " + player)
#             print("You win", player, "covers", computer)
#         if computer == "scissors":
#             print("computer: " + computer)
#             print("player: " + player)
#             print("You lose", computer, "cuts", player)
#     elif player == "scissors":
#         if computer == "paper":
#             print("computer: " + computer)
#             print("player: " + player)
#             print("You win", player, "cuts", computer)
#         if computer == "rock":
#             print("computer: " + computer)
#             print("player: " + player)
#             print("You lose", computer, "smashes", player)
#     play_again = input("Play again? (yes/no): ").lower()
#     if play_again != "yes":
#         break
#
# print("Bye!")

# def new_game():
#     guesses = []
#     correct_guesses = 0
#     question_num = 1
#
#     for key in questions:
#         print("-----------------------------")
#         print(key)
#         for i in options[question_num - 1]:
#             print(i)
#         guess = input("Enter (A, B, C, or D): ").upper()
#         guesses.append(guess)
#
#         correct_guesses += check_answer(questions.get(key), guess)
#         question_num += 1
#
#     display_score(correct_guesses, guesses)
#
#
# def check_answer(answer, guess):
#     if answer == guess:
#         print("CORRECT!")
#         return 1
#     else:
#         print("WRONG!")
#         return 0
#
# def display_score(correct_guesses, guesses):
#     print("-----------------------------")
#     print("RESULTS")
#     print("-----------------------------")
#
#     print("Answers: ", end="")
#     for i in questions:
#         print(questions.get(i), end=" ")
#     print()
#
#     print("Guesses: ", end="")
#     for i in guesses:
#         print(i, end=" ")
#     print()
#
#     score = int((correct_guesses/len(questions))*100)
#     print("Your score is: " + str(score) + "%")
#
# def play_again():
#     response = input("Do you want to play again? (yes or no): ").lower()
#     if response == "yes":
#         return True
#     else:
#         return False
#
# questions = {
#     "Who created Python?: ": "A",
#     "What year was Python created?: ": "B",
#     "Python is tributed to which comedy group?: ": "C",
#     "Is the Earth round?: ": "A",
# }
#
# options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
#           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
#           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
#           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]
#
# new_game()
# while play_again():
#     new_game()
# print("Bye!")


