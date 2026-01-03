##tuple is an unordered but immutable(that means non-changeable/it cannot be changed) the sequence of elements written inside parenthesis '()'

tup1 = ("rajat", 45, "singapore", True, 56.6)
print(type(tup1))  #will print <class 'tuple'>

#To make an empty tuple
tup2 = (1,)  #note-here comma(,)is important to be put
tup3 = (1)

print(type(tup2))  #will print <class 'tuple'>
print(type(tup3))  #will print <class 'int'>

#Immutability
# tup1[2] = "shubham"  #this will give an error and no changes will occur


## PROPERTIES OF TUPLE

numbers = (1, 4, 8, 3, 4, 7, 5, 8, 2)

# 1. .count(element)-counts the no. of times an element occured in the tupple
print(numbers.count(4))  #will print '2'

# 2. .index(element)-returns the index of first occurence of element in the tuple
print(numbers.index(4))  #will print '1' as the index of first occurence of it

# 3. concatenation
tuple1 = (1,3,5)
tuple2 = (2,4,6)
concatenate = tuple1 + tuple2
print(concatenate)