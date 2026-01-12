#BREAK Statement - it breaks the loop after a specified situation is achieved
for i in range(1,11):
    if i == 7:  #whenever the loop will reach 'i==7', it will break the loop
        break
    print(i)


# CONTINUE Statement - it skips the specified value and continues the loop to iterate
for i in range(1,11):
    if i == 7:  #whenever the loop will reach 'i==7', it will skip the value '7' and the loop will continue
        continue
    print(i)


# PASS Statement - it skips the specified value and continues the loop to iterate
#for i in range(1,11):  #(it will give error)agar kabhi hume nahi malum ho ki kya code likhna hai ya hum confused hon aur isi(next line)
# situation me code ko chhodna padd jaye bina kisi error ke sath toh, hum 'pass' statement ka use krte hain

for i in range(1,11):
    pass 
# 'pass' statement just means that if and whenever you are not sure and don't want to write the code and execute it without any error, you use 'pass' statement
