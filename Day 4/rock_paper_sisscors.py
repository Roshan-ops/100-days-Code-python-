import random


game=["It's rock","It's paper","It's sissors" ]
paper = "It's Paper"
rock =" It's rock"
sissors= "It's sissors"
play = int (input ("Enter you picks between three of them"))
if play >= 3 and play < 0:
    print("You have enter the invalid number")

else:
    print(game[play])
    
computer_play = random.randint(0 , 2)
print (" Comuter have chose:")
print(game[computer_play])

if play == 0 and computer_play ==2:
    print("you win!")
elif computer_play == 0 and play == 2:
    print("You lose")
elif computer_play > play:
    print(" You lose")
elif play > computer_play:
    print("you win! ")
elif computer_play == play :
    print("It's a draw")
