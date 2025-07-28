import random
import time
z="Yes"
while z=="Yes":
    turns=0
    x=[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print(x[0])
    print(x[1])
    print(x[2])
    while True:
        x1=int(input("What is the x-coord of where you would like to move?"))
        y1=int(input("What is the y-coord of where you would like to move?"))
        while x[x1][y1]=="x" or x[x1][y1]=="o":
            print("That move is illegal! Choose a different move.")
            x1=int(input("What is the x-coord of where you would like to move?"))
            y1=int(input("What is the y-coord of where you would like to move?"))
        x[x1][y1]="x"
        print(x[0])
        print(x[1])
        print(x[2])
        print()
        if x[0][0]=="x" and x[0][1]=="x" and x[0][2]=="x":
            print("Congratulations! You win!!!")
            break
        if x[1][0]=="x" and x[1][1]=="x" and x[1][2]=="x":
            print("Congratulations! You win!!!")
            break
        if x[2][0]=="x" and x[2][1]=="x" and x[2][2]=="x":
            print("Congratulations! You win!!!")
            break
        if x[0][0]=="x" and x[1][0]=="x" and x[2][0]=="x":
            print("Congratulations! You win!!!")
            break
        if x[0][1]=="x" and x[1][1]=="x" and x[2][1]=="x":
            print("Congratulations! You win!!!")
            break
        if x[0][2]=="x" and x[1][2]=="x" and x[2][2]=="x":
            print("Congratulations! You win!!!")
            break
        if x[0][0]=="x" and x[1][1]=="x" and x[2][2]=="x":
            print("Congratulations! You win!!!")
            break
        if x[2][0]=="x" and x[1][1]=="x" and x[0][2]=="x":
            print("Congratulations! You win!!!")
            break
        turns+=1
        if turns==5:
            print("This game ended in a tie!")
            break
        time.sleep(1)
        x2=random.randint(0,2)
        y2=random.randint(0,2)
        while x[x2][y2]=="x" or x[x2][y2]=="o":
            x2=random.randint(0,2)
            y2=random.randint(0,2)
        x[x2][y2]="o"
        print(x[0])
        print(x[1])
        print(x[2])
        if x[0][0]=="o" and x[0][1]=="o" and x[0][2]=="o":
            print("Womp womp. You lost. ):")
            break
        if x[1][0]=="o" and x[1][1]=="o" and x[1][2]=="o":
            print("Womp womp. You lost. ):")
            break
        if x[2][0]=="o" and x[2][1]=="o" and x[2][2]=="o":
            print("Womp womp. You lost. ):")
            break
        if x[0][0]=="o" and x[1][0]=="o" and x[2][0]=="o":
            print("Womp womp. You lost. ):")
            break
        if x[0][1]=="o" and x[1][1]=="o" and x[2][1]=="o":
            print("Womp womp. You lost. ):")
            break
        if x[0][2]=="o" and x[1][2]=="o" and x[2][2]=="o":
            print("Womp womp. You lost. ):")
            break
        if x[0][0]=="o" and x[1][1]=="o" and x[2][2]=="o":
            print("Womp womp. You lost. ):")
            break
        if x[2][0]=="o" and x[1][1]=="o" and x[0][2]=="o":
            print("Womp womp. You lost. ):")
            break
    z=input("Would you like to play again?")
    if z=="No":
        print("Alright, so long!")