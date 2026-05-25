import random
choice=["rock","paper","scissor"]
computer=random.choice(choice)
player=input("enter rock,paper or scissor:").lower()
if player==computer:
     print("it is tie!")
elif player=="rock" and computer=="scissor":
     print("you win")
elif player=="paper" and computer=="rock":
     print("you win")
elif player=="scissor" and computer=="paper":
     print("you win")
else:
     print("computer win")
print("Computer guess is:",computer)
    

    
