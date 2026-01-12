##list is an unordered and mutable(that means changeable/it can be changed) the sequence of elements written inside square brackets '[]'

friends = ["rahul", "akash", "payal", "mohit", "roshni", "suraj"]  #this is a list
print(friends)


# #PROPERTIES OF LIST

# 1.finding the elements from a list of a certain index
print(friends[2])  #will print "payal" as the indexing is started from 0 which is "akash"

# 2.finding the length of the list
print(len(friends))  #will print '6'

# 3.lists can be edited after they are made unlike the strings
friends[4] = "rohit"
print(friends)  #will print ['rahul', 'akash', 'payal', 'mohit', 'rohit', 'suraj']


#METHODS OF LIST

numbers = [3,56,17,80,6,63]

# 1. .sort() - sorts the list in ascending order
numbers.sort()  #the list is just sorted at this stage
print(numbers)  #now it will be printed as [3,6,17,56,63,80]

# 2. .reverse() - reverses the unordered list
numbers.reverse()
print(numbers)  #will print [63, 6, 80, 17, 56, 3]

# 3. .append() - used to add elements to the last of the list
numbers.append(44)   #adds the element '44' at the end of the list
print(numbers)  #prints [3, 56, 17, 80, 6, 63, 44]

# 4. .insert(index,element) - used to add an element at a fix index
numbers.insert(3,79)  #will add 79 between '17' and '80'
print(numbers)  #will print [3, 56, 17, 79, 80, 6, 63]

# 5. .pop(mention_the_index) - removes element at index and returns the value of remaining list
numbers.pop(2)  #removes '17' which is at index '2'
print(numbers)  #will print [3, 56, 80, 6, 63]

# 6. .remove(mention_the_element) - removes element and returns the value of remaining list
numbers.remove(56)  #removes element '56' from the list
print(numbers)  #will print [3, 17, 80, 6, 63]

#EXTRA
#to form an empty list syntax will be
list = [1]
print(list)
