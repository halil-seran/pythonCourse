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










