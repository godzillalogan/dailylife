#Rock paper Scissors game
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

You=int(input("What do you choose?Rock, Type 1 for Rock, 2 for Paper oe 3 for Scissors.\n"))
computer=random.randint(1,3)

  
if You==1 or You==2 or You==3:
  #print your image
  print("You:")
  if You==1:
    print(rock)
  elif You==2:
    print(paper)
  elif You==3:
    print(scissors)

  #print computer image
  print("Computer:")
  if computer==1:
    print(rock)
  elif computer==2:
    print(paper)
  elif computer==3:
    print(scissors) 

  #draw condition
  if You==1 and computer==1:
    print("it is a draw")
  elif You==2 and computer==2:
    print("it is a draw")
  elif You==3 and computer==3:
    print("it is a draw")

  #You win condition
  elif You==1 and computer==3:
    print("You win")
  elif You==2 and computer==1:
    print("You win")
  elif You==3 and computer==2:
    print("You win")

  #computer win condition
  elif You==1 and computer==2:
    print("You lose")
  elif You==2 and computer==3:
    print("You lose")
  elif You==3 and computer==1:
    print("You lose")

#if you type not 1 or 2 or 3 condition
else:
  print("Please type 1 for Rock, 2 for Paper oe 3 for Scissors.")

