import random
x=random.randint(1,10)
y=0
a=int(input("I thought of a random number 1-10! What's your guess?"))
if a==x:
    y=1
    print("Wow! You guessed correctly first try!")
if y!=1:
    a=int(input("Wrong! Give me another number 1-10, and I'll tell you if it's lower or higher than my number... or the same!"))
    if a==x:
        y=1
        print("No way! That's my number! Nicely done!")
    elif a>x:
        print("That number is greater than mine!")
    elif a<x:
        print("That number is less than mine!")
if y!=1:
    a=input("Alright. How about this? Guess whether the number is even or odd, and I'll tell you if you're right or wrong!")
    if a=="Odd" and x%2==1:
        print("Right! My number is odd!")
    elif a=="Odd" and x%2==0:
        print("Wrong! My number is not odd!")
    elif a=="Even" and x%2==0:
        print("Right! My number is even!")
    elif a=="Even" and x%2==1:
        print("Wrong! My number is not even!")
    a=int(input("Well, it's time for your final guess. What do you think my number is?"))
    if a==x:
        print("That is........... MY NUMBER!!! Congratulations!")
    else:
        print("That is........... NOT MY NUMBER!!! Womp womp. My number was "+str(x)+".")