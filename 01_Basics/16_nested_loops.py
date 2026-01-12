# We have to print the following pattern
# *
# **
# ***
# ****
# *****

#ANSWER- for it we will use nested for loop

rows = int(input("Enter the number of rows you need: "))

for i in range(1,rows+1):
    for j in range(0,i):
        print("*", end=" ")
    print("")
