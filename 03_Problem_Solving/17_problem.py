f = int(input("Enter first number: "))
s = int(input("Enter second number: "))
t = int(input("Enter third number: "))

def greatest():
    if(f>s and f>t):
        return "First number is greatest"
    elif(s>f and s>t):
        return "Second number is greatest"
    elif(t>f and t>s):
        return "Third number is greatest"
    else:
        return "None is greatest"

print(greatest())