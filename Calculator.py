b="Yes"
while b=="Yes":
    x=int(input("What's your first number?"))
    y=int(input("What's your second number?"))
    p=input("Would you like a third number?")
    if p=="Yes":
        z=int(input("What's your third number?"))
    a=input("What operation would you like to use?")
    while a!="Addition" and a!="Multiplication" and a!="Division" and a!="Subtraction":
        a=input("Hey! Not a valid operation! Gimme another!")
    if p=="No" and (a=="Addition" or a=="Subtraction"):
        z=0
    elif p=="No" and (a=="Multiplication" or a=="Division"):
        z=1
    if a=="Addition":
        print(x+y+z)
    elif a=="Multiplication":
        print(x*y*z)
    elif a=="Division":
        print(x/y/z)
    elif a=="Subtraction":
        print(x-y-z)
    b=input("Would you like me to calculate something else?")
    if b=="No" or b=="Nope":
        print("Then get out of here!")