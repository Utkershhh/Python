#set is a collection of non-repetitive elements and it is immutable
s1 = set()   #empty set, because set and dictionary both are written within '{}' brackets
print(type(s1))  #<class 'set'>

s2 = {"Rahul", 24, "delhiisthecapital", 45.67, True, 24, 24, 24}   #still it will return '24' only one time as value are non-repetitive in  a dictionary
print(s2)

# METHODS OF SETS

# 1. .add()-to add values
s2.add("Argentina")
print(s2)

# 2. .len(set_name)-same work
print(len(s2))

# 3. .remove(element)-to remove the specified element
s3 = {1,4,7,16,23}
# s3.remove(16)
# print(s3)

# 4. .pop()-removes an random element and returns the element removed
print(s3.pop())
# print(s3)
