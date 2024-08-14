print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Cave.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a cave. '
                    'There is are two paths in the cave. One leads upwards and the other downwards'
                    'Type "up" to climb up. '
                    'Type "down" to take the slope downwards.\n').lower()
    if choice2 == "up":
        choice3 = input("You arrive at a lake within the cave unharmed. "
                        "There is a house carved out of stone with 3 doors. One with a star on it , "
                        "one with a gun on it and one with a cat on it. "
                        "Which door do you choose? The one with the Star, Gun or Cat? ...\n").lower()
        if choice3 == "star":
            print("It's a room full of fire. Game Over")
        elif choice3 == "gun":
            print("You found the treasure. You Win!")
        elif choice3 == "cat":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist The walls caved in and crushed you.\n Game Over.")
    else:
        print("You got attacked by an angry Bats, they suck all your blood.\n Game Over.")

else:
    print("You fell in to a hole and are trapped... You starved.\n Game Over.")
