import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# import time and user time.sleep(1) to add a 1 second delay between rock paper scissors and shoot print statements.
print(f"{rock}!")
print(f"{paper}!")
print(f"{scissors}!")
print(f"Shoot!!")

player_choose = int(input("What do you choose?\n Type 0 for ROCK OR,\n Type 1 for PAPER OR \n Type 2 for SCISSORS\n "))
robot_choose = random.randint(0, 2)

match player_choose, robot_choose:

    case 0, 0:
        print(f"you chose: {rock}")
        print(f"Robot chose: {rock}")
        print("That's a draw!")
    case 1, 1:
        print(f"you chose: {paper}")
        print(f"Robot chose: {paper}")
        print("That's a draw!")
    case 2, 2:
        print(f"you chose: {scissors}")
        print(f"Robot chose: {scissors}")
        print("That's a draw!")
    case 0, 1:
        print(f"you chose: {rock}")
        print(f"Robot chose: {paper}")
        print("Paper beats rock! sorry you lose...")
    case 1, 0:
        print(f"you chose: {paper}")
        print(f"Robot chose: {rock}")
        print("Paper beats rock! You win!!")
        print('''

              .-=========-.
             \_'-=======-'_/
              _|   .=.   |_
             ((|  {{1}}  |))
              \|   /|\   |/
               \__ '`' __/
                 _`) (`_
               _/_______\_
             _/___________\_

                ''')
    case 2, 0:
        print(f"you chose: {scissors}")
        print(f"Robot chose: {rock}")
        print("Rock beats scissors! sorry you lose...")
    case 0, 2:
        print(f"you chose: {rock}")
        print(f"Robot chose: {scissors}")
        print("Rock beats scissors! You win!!!")
        print('''

              .-=========-.
             \_'-=======-'_/
              _|   .=.   |_
             ((|  {{1}}  |))
              \|   /|\   |/
               \__ '`' __/
                 _`) (`_
               _/_______\_
             _/___________\_

                ''')
    case 1, 2:
        print(f"you chose: {paper}")
        print(f"Robot chose: {scissors}")
        print("Scissors beats Paper! sorry you lose...")
    case 2, 1:
        print(f"you chose: {scissors}")
        print(f"Robot chose: {paper}")
        print("Scissors beats Paper! you win!!")
        print('''
        
              .-=========-.
             \_'-=======-'_/
              _|   .=.   |_
             ((|  {{1}}  |))
              \|   /|\   |/
               \__ '`' __/
                 _`) (`_
               _/_______\_
             _/___________\_
              
        ''')
    case _:
        print("invalid number entered, you tried to cheat so you lose!!")
