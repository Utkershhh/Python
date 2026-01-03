#conversion of temperature from degree to farenhiet

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in farenhiet: "))
print(f_to_c(f))