# import random
#
# def rollDice():
#     return random.randint(1,6)
#
# def main():
#     player1 = 0
#     player2 = 0
#     turn = 0
#     while player1 < 100 and player2 < 100:
#         if turn == 0:
#             print("Player 1's turn")
#             print("Current score of player 1: ", player1)
#             print("Current score of player 2: ", player2)
#             print("Rolling dice...")
#             dice = rollDice()
#             print("Dice value: ", dice)
#             if dice == 1:
#                 print("You rolled a 1. Your turn is over.")
#                 turn = 1
#             else:
#                 player1 += dice
#                 print("Your score is now: ", player1)
#                 print("Would you like to roll again? (y/n)")
#                 choice = input()
#                 if choice == 'n':
#                     turn = 1
#         else:
#             print("Player 2's turn")
#             print("Current score of player 1: ", player1)
#             print("Current score of player 2: ", player2)
#             print("Rolling dice...")
#             dice = rollDice()
#             print("Dice value: ", dice)
#             if dice == 1:
#                 print("You rolled a 1. Your turn is over.")
#                 turn = 0
#             else:
#                 player2 += dice
#                 print("Your score is now: ", player2)
#                 print("Would you like to roll again? (y/n)")
#                 choice = input()
#                 if choice == 'n':
#                     turn = 0
#     if player1 >= 100:
#         print("Player 1 wins!")
#     else:
#         print("Player 2 wins!")
#
# main()
# x = 100
#
# reverse = str(x)[::-1]
# int(reverse)
#
# print(reverse)
#
# txt = "Hello World" [::-1]
# print(txt)

# list = ["a", "b", "c", "d", "e", "f", "g", "h"]
# #
# for i in list:
#     print(i[0])


