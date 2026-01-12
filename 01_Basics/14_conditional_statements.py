#IF-ELSE

'''the 'if' statement is used to provide a condition and 'else' is used to used to define the remaining condition after the loop
does not satisfies the 'if'condition.'''

number = int(input("Enter a number: "))
if(number>50):
    print("Number is greater than 50")
else:
    print("Number is smaller than 50")


#ELIF(else-if)

'''it is used to when none of the conditions satisfy'''

number = int(input("Enter a number: "))
if(number>500):
    print(number, "Aur it is greater than 500")
elif(number==500):
    print(number, "Aur it is equal to 500")    
else:
    print(number, "Aur it is smaller than 500")


'''above is a machine for determining numbers less than, greater than, or equal to 500 by using if, else and
elif(else-if)statements.There can be as many elif statements.'''



#NESTED IF-ELSE

number = int(input("Enter a number: "))
if(number>0):
    print("Chalo no. toh sahi format me enter kra hai, ab suno no. hai kya")
    if(number>500):
        print("Number", number, "hai aur it is greater than 500")
    elif(number==500):
        print("Number", number, "hai aur it is equal to 500")    
    else:
        print("Number", number, "hai aur it is smaller than 500")
else:
    print("No. toh +ve daal do maharaj")
