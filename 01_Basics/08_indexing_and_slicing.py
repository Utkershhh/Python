#INDEXING - means numbering of strings starting from '0' to 'n' and to find index we use keyword variablename.index(string)

a = "LucknowisthecapitalofUttarPradesh"
a.index("h")
print(a.index("h")) #this will tell at which index is the certain word or alphabet used at


#SLICING - POSITIVE SLICING - meaning that taking out a certain peace[a,n] of string from the whole string starting from a to n-1 index 

student = "He is the brightest student of the class"
slicing = student[3:9]
print(student[3:9]) #this includes slicing from the index 3 to 8 as told above

# NEGATIVE SLICING - meaning that taking out a certain peace[-a,-n] of string from the whole string starting from a to n-1 element but this time reversing the side and starting the counting of indexing from '-1' in place of '0' 

b = "This time it is reversed bhaiyon"
slicing2 = b[-16:-8]
print(b[-16:-8])

#NOTE

slicing3 = b[:5]    #is same as [0:5]
slicing4 = b[25:]   #is same as [25:41] i.e. to the last element

#slicing with skip value

slicing5 = b[0:23:2] #that means moving to the 22nd element with steps/gap of 3 elements[start:stop:step]
print(b[0:23:2])