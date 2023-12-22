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

# from car import Car
#
# car_1 = Car("Chevrolet", "Camaro", 2021, "red")
# car_2 = Car("Mercedes", "C300", 2020, "black")

# print(car_1.make)
# print(car_1.model)
# print(car_2.year)
# print(car_2.color)
#
# car_1.drive()
# car_2.stop()
# Car.wheels = 6
# print(car_1.wheels)
# print(Car.wheels)


# class Animal:
#
#     alive: True
#
#     def eat(self):
#         print("This animal is eating")
#
#     def sleep(self):
#         print("This animal is sleeping")
#
#
# class Rabbit(Animal):
#     def run(self):
#         print("This rabbit is running")
#
#
# class Fish(Animal):
#     def swim(self):
#         print("This fish is swimming")
#
#
# class Hawk(Animal):
#     def fly(self):
#         print("This hawk is flying")
#
#
# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()
# print(rabbit.alive)
# fish.eat()
# hawk.sleep()
# rabbit.run()
# fish.swim()
# hawk.fly()

# class Organism:
#     alive = True
#
# class Animal(Organism):
#     def eat(self):
#         print("This animal is eating")
#
# class Dog(Animal):
#     def bark(self):
#         print("This dog is barking")
#
# dog = Dog()
# print(dog.alive)
# dog.eat()
# dog.bark()

# class Prey:
#     def flee(self):
#         print("This animal is fleeing")
#
# class Predator:
#     def hunt(self):
#         print("This animal is hunting")
#
# class Rabbit(Prey):
#     pass
#
# class Hawk(Predator):
#     pass
#
# class Fish(Prey, Predator):
#     pass
#
# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()
#
# rabbit.flee()
# hawk.hunt()
# fish.flee()
# fish.hunt()

# class Animal:
#     def eat(self):
#         print("This animal is eating")
#
#
# class Fish(Animal):
#     def eat(self):
#         print("This fish is eating")
#
#
# fish = Fish()
# fish.eat()


# class Car:
#
#     def turn_on(self):
#         print("You start the engine")
#         return self
#
#     def drive(self):
#         print("You drive the car")
#         return self
#
#     def brake(self):
#         print("You step on the brake")
#         return self
#
#     def turn_off(self):
#         print("You turn off the engine")
#         return self
#
#
#
# car = Car()

# car.turn_on()
# car.drive()
#
# car.turn_on().drive()

# (car.turn_on().
#  drive().
#  brake().
#  turn_off())

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
# class Square(Rectangle):
#     def __init__(self, side_length):
#         super().__init__(side_length, side_length)
#     def area(self):
#         return self.width * self.height
# class Cube(Square):
#     def surface_area(self):
#         face_area = super().area()
#         return face_area * 6
#     def volume(self):
#         face_area = super().area()
#         return face_area * self.height
#
# square = Square(4)
# cube = Cube(3)
# print(square.area())
# print(cube.surface_area())

# from abc import ABC, abstractmethod
#
#
# class Vehicle(ABC):
#
#     @abstractmethod
#     def go(self):
#         pass
#
#     @abstractmethod
#     def stop(self):
#         pass
#
#
# class Car(Vehicle):
#     def go(self):
#         print("You drive the car")
#
#     def stop(self):
#         print("You stop the car")
#
#
# class Motorcycle(Vehicle):
#     def go(self):
#         print("You ride the motorcycle")
#
#     def stop(self):
#         print("You stop the motorcycle")
#
#
# # vehicle = Vehicle()
# car = Car()
# motorcycle = Motorcycle()
#
# # vehicle.go()
# car.go()
# motorcycle.go()
# car.stop()
# motorcycle.stop()

# class Car:
#     color = None
#
# class Motorcycle:
#     color = None
#
# def change_color(car, color):
#     car.color = color
#
# car1 = Car()
# car2 = Car()
# car3 = Car()
#
# bike1 = Motorcycle()
#
# change_color(car1, "red")
# change_color(car2, "blue")
# change_color(car3, "green")
# change_color(bike1, "black")
#
#
# print(car1.color)
# print(car2.color)
# print(car3.color)
# print(bike1.color)


# class Duck:
#     def walk(self):
#         print("This duck is walking")
#
#     def talk(self):
#         print("This duck is quacking")
#
#
# class Chicken:
#     def walk(self):
#         print("This chicken is walking")
#
#     def talk(self):
#         print("This chicken is clucking")
#
# class Person():
#     def catch(self, duck):
#         duck.walk()
#         duck.talk()
#         print("You caught the critter")
#
#
# duck = Duck()
# chicken = Chicken()
# person = Person()
#
# person.catch(duck)
# person.catch(chicken)

# happy = True
# print(happy)

# print(happy := True)
#
# foods = list()
# while True:
#     food = input("Enter a food to remember. Enter 'end' to quit: ")
#     if food == "end":
#         break
#     foods.append(food)

# foods = list()
# while food := input("Enter a food to remember. Enter 'end' to quit: ") != "end":
#     foods.append(food)


# def hello():
#     print("Hello")
#
# hello()
# print(hello)
# hi = hello
# print(hi)
# hi()

# say = print
#
# say("Hello")


# def loud(text):
#     return text().upper()
#
#
# def quiet(text):
#     return text().lower()
#
#
# def hello(func):
#     text = func("Hello")
#     print(text)
#
# hello(loud)
# hello(quiet)

# def divisor(x):
#     def dividend(y):
#         return y / x
#     return dividend
#
# divide = divisor(2)
# print(divide(10))


# def double(x):
#     return x * 2
#
# print(double(12))

# double = lambda x: x * 2
# multiply = lambda x, y: x * y
# add = lambda x, y, z: x + y + z
# full_name = lambda first, last: first + " " + last
# age_check = lambda age: True if age >= 18 else False
#
# print(double(12))
# print(multiply(12, 2))
# print(add(12, 2, 4))
# print(full_name("Halil", "seran"))
# print(age_check(25))


# students = ["Squidward", "Spongebob", "Patrick", "Sandy", "Mr. Krabs"]
# students2 = ("Squidward", "Spongebob", "Patrick", "Sandy", "Mr. Krabs")
#
# students.sort(reverse=True)
# sorted_students = sorted(students2, reverse=True)
#
#
# print(students)
# print(sorted_students)

# students = [("Squidward", "F", 50),
#            ("Spongebob", "A", 20),
#            ("Patrick", "D", 35),
#            ("Sandy", "B", 25),
#            ("Mr. Krabs", "C", 100)]
#
# grade = lambda grades: grades[1]
# age= lambda ages: ages[2]
#
# students.sort(key=grade, reverse=True)
# students.sort(key=age)
#
# print(students)

# students = (("Squidward", "F", 50),
#            ("Spongebob", "A", 20),
#            ("Patrick", "D", 35),
#            ("Sandy", "B", 25),
#            ("Mr. Krabs", "C", 100))
#
# grade = lambda grades: grades[1]
# age= lambda ages: ages[2]
# sorted_students = sorted(students, key=age)
#
# print(sorted_students)

# store = [("shirt", 20.00),
#          ("pants", 25.00),
#          ("jacket", 50.00),
#          ("socks", 10.00)]
#
# to_euros = lambda data: (data[0], data[1] * 0.92)
# to_dollars = lambda data: (data[0], data[1] / 0.92)
#
# store_euros = list(map(to_euros, store))
# store_dollars = list(map(to_dollars, store_euros))
#
# for i in store_euros:
#     print(i)
# for i in store_dollars:
#     print(i)


# friends = [("Rachel", 19),
#               ("Monica", 18),
#               ("Phoebe", 17),
#               ("Joey", 16),
#               ("Chandler", 21),
#               ("Ross", 20)]
#
# age = lambda data: data[1] >= 18
#
# drinking_buddies = list(filter(age, friends))
#
# print(drinking_buddies)


# import functools


# letters = ["H", "A", "L", "I", "L"]
#
# word = functools.reduce(lambda x, y: x + y, letters)
#
# print(word)

# factorial = [5, 4, 3, 2, 1]
#
# result = functools.reduce(lambda x, y: x * y, factorial)
# print(result)

# squares = []
#
# for i in range(1, 11):
#     squares.append(i * i)
#
# print(squares)
#
# squares = [i * i for i in range(1, 11)]
# print(squares)


# students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
#
# passed_students = list(filter(lambda x: x >= 60, students))
#
# passed_students2 = [i for i in students if i >= 60]
#
# failed_students = list(filter(lambda x: x < 60, students))
#
# print(passed_students)
# print(passed_students2)
# print(failed_students)

# cities_in_F = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
#
# cities_in_C = {key: round((value - 32) * (5/9)) for (key, value) in cities_in_F.items()}
#
# print(cities_in_C)
#
# weather = {"New York": "snowing", "Boston": "sunny", "Los Angeles": "sunny", "Chicago": "cloudy"}
#
# sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
#
# print(sunny_weather)
#
# cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
#
# desc_cities = {key: ("warm" if value >= 40 else "cold") for (key, value) in cities.items()}
#
# print(desc_cities)

# cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
#
# def check_temp(value):
#     if value < 40:
#         return "cold"
#     elif value >= 40 and value < 60:
#         return "mild"
#     else:
#         return "warm"
#
# desc_cities = {key: check_temp(value) for (key, value) in cities.items()}
#
# print(desc_cities)

# usernames = ['jon', 'tyrion', 'theon', 'cersei', 'sansa']
# passwords = ("jon123", "tyrion123", "theon123", "cersei123", "sansa123")
# login_date = [2012, 2013, 2014, 2015, 2016]
#
#
# users = zip(usernames, passwords, login_date)
# users2 = list(zip(usernames,passwords))
#
# for i in users:
#     print(i)


# def main():
#     print("main function")
#
#
# if __name__ == "__main__":
#     main()


# import time

# print(time.ctime(1000000000))
#
# print(time.time())
#
# print(time.ctime(time.time()))
#
# time_object = time.localtime()
# print(time_object)
#
# local_time = time.strptime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)
#
# time_string = "11 September, 2001"
# time_object2 = time.strptime(time_string, "%d %B, %Y")
# print(time_object2)

# time_tuple = (2021, 9, 11, 9, 11, 0, 5, 254, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)

# time_tuple = (2021, 9, 11, 9, 11, 0, 5, 254, 0)
# time_string = time.mktime(time_tuple)
# print(time_string)

# import threading
# import time
#
#
# def eat_breakfast():
#     time.sleep(3)
#     print("You finished eating breakfast")
#
#
# def drink_coffee():
#     time.sleep(4)
#     print("You finished drinking coffee")
#
#
# def study():
#     time.sleep(5)
#     print("You finished studying")
#
#
# x = threading.Thread(target = eat_breakfast, args=())
# x.start()
#
# y = threading.Thread(target = drink_coffee, args=())
# y.start()
#
# z = threading.Thread(target = study, args=())
# z.start()
#
#
# x.join()
# y.join()
# z.join()

# eat_breakfast()
# drink_coffee()
# study()


# print(threading.active_count())
# print(threading.enumerate())
# print(time.perf_counter())


# import threading
# import time
#
#
# def timer():
#     print()
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print("Logged in for: ", count, "seconds")
#
#
# x = threading.Thread(target=timer, daemon=True)
# x.start()
#
# x.setDaemon(True)
# print(x.isDaemon())
#
# answer = input("Do you wish to exit? ")


# from multiprocessing import Process, cpu_count
# import time
#
#
# def counter(num):
#     count = 0
#     while count < num:
#         count += 1
#
# def main():
#
#     print(cpu_count())
#
#     a = Process(target=counter, args=(100000000,))
#     b = Process(target=counter, args=(100000000,))
#     c = Process(target=counter, args=(100000000,))
#     d = Process(target=counter, args=(100000000,))
#     e = Process(target=counter, args=(100000000,))
#     f = Process(target=counter, args=(100000000,))
#     g = Process(target=counter, args=(100000000,))
#     h = Process(target=counter, args=(100000000,))
#
#     a.start()
#     b.start()
#     c.start()
#     d.start()
#     e.start()
#     f.start()
#     g.start()
#     h.start()
#
#
#     a.join()
#     b.join()
#     c.join()
#     d.join()
#     e.join()
#     f.join()
#     g.join()
#     h.join()
#
#
#     print("Finished in: ", time.perf_counter(), "seconds")
#
# if __name__ == '__main__':
#     main()


# from tkinter import *

# window = Tk()
# window.geometry("420x420")
# window.title("My GUI")

# icon = PhotoImage(file='icon.jpg')
# window.iconphoto(True, icon)
# window.config(background="#5cffd6")

# window.mainloop()


# window = Tk()
# window.geometry("420x420")
# window.title("My GUI")
#
# label = Label(window, text="halil seran!", font=("Arial", 40, "bold"), fg="white", bg="black")
# label.place(x=0,y=0)


# window.mainloop()

# from tkinter import *
#
#
# count = 0
# def click():
#     global count
#     count += 1
#     print("Button was clicked " + str(count) + " times")
#
# window = Tk()
# # photo = PhotoImage(file="icon.jpg")
#
# button = Button(window,
#                 text="Click Me!",
#                 width=20,
#                 height=5,
#                 bg="black",
#                 fg="white",
#                 font=("Arial", 20, "bold"),
#                 command=click,
#                 activeforeground="red",
#                 activebackground="blue",
#                 state=ACTIVE,
#                 # image=photo,
#                 # compound="bottom",
#                 )
# button.pack()
#
# window.mainloop()

    # from tkinter import *
    # from tkinter import filedialog
    #
    # def openFile():
    #     filepath = filedialog.askopenfile()
    #     print(filepath)
    #
    # window = Tk()
    #
    # button = Button(text="Open File", command=openFile)
    # button.pack()
    #
    #
    #
    # window.mainloop()

#
# nums = [2,7,11,15]
# target = 9
#
# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if(nums[i] + nums[j] == target):
#                 return [i,j]
#
#
#
# twoSum(nums, target)

# l1 = [2,4,3]
# l2 = [5,6,4]
#
# def addTwoNumbers(l1, l2):
#     l1.reverse()
#     l2.reverse()
#     l1 = int("".join(map(str, l1)))
#     l2 = int("".join(map(str, l2)))
#     sum = l1 + l2
#     sum = str(sum)
#     sum = list(sum)
#     sum.reverse()
#     return sum











