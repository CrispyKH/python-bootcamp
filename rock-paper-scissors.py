import random
#Rock Paper Scissors Game
user_choose = int(input("What do you choose? Type 0 for 'rock', 1 for 'paper' 2 for 'scissors': ")) #0 = rock, 1 = paper, 2 = scissors
computer_choose = random.randint(0,2)
#Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
#Paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
#Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
print("You chose: ")
print(game_images[user_choose]) #IMPORTANT -- this line prints the image based on the user input (0, 1, or 2) ***saves time from multiple print statements
                                #try to think in lists and arrays to make code more efficient and universal
if computer_choose == 0:
    print(f"Computer chose: {rock}")
    if user_choose == 0:
        print("It's a draw")
    elif user_choose == 1:
        print("You win!")
    elif user_choose == 2:
        print("You lose!")
    else:
        print("Invalid input, you lose!")
elif computer_choose == 1:
    print(f'Computer chose: {paper}')
    if user_choose == 0:
        print("You lose!")
    elif user_choose == 1:
        print("It's a draw")
    elif user_choose == 2:
        print("You win!")
    else:
        print("Invalid input, you lose!")
elif computer_choose == 2:
    print(f'Computer chose: {scissors}')
    if user_choose == 0:
        print("You win!")
    elif user_choose == 1:
        print("You lose!")
    elif user_choose == 2:
        print("It's a draw")
    else:
        print("Invalid input, you lose!")