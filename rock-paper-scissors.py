import random
#Rock Paper Scissors Game
user_choose = input("What do you choose? Type 0 for 'rock', 1 for 'paper' 2 for 'scissors': ") #0 = rock, 1 = paper, 2 = scissors
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
if computer_choose == 0:
    print("Computer chose: {rock}")
    if user_choose == 0:
        print("It's a draw")
    elif user_choose == 1:
        print("You win!")
    elif user_choose == 2:
        print("You lose!")
    else:
        print("Invalid input, you lose!")
'''
elif computer_choose == 1:
    print('Computer chose: "paper"')
    if user_choose == "rock":
        print("You lose!")
    elif user_choose == "paper":
        print("It's a draw")
    elif user_choose == "scissors":
        print("You win!")
    else:
        print("Invalid input, you lose!")
elif computer_choose == 2:
    print('Computer chose: "scissors"')
    if user_choose == "rock":
        print("You win!")
    elif user_choose == "paper":
        print("You lose!")
    elif user_choose == "scissors":
        print("It's a draw")
    else:
        print("Invalid input, you lose!")
        '''