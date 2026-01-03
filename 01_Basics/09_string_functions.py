#there are certain in-built functions to manupilate or perform operations in python

str = "delhiisaverypollutedunionterritory"

# 1.len() - for printing the length of the string
len(str)
print(len(str))


# 2. .endswith() - used for finding if our string is ending with certain another string or group of strings and will print True/False
str.endswith("insane")
print(str.endswith("insane"))  #will print False

str.endswith("tory")
print(str.endswith("tory"))  #will print True


# 3. .count(the_element_or_string_that_is_to_be_counted) - this counts the number of certain string or element in any other string
str.count("i")
print(str.count("i"))  #will print '4' as the 'i' is repeated 4 times in the value of 'str' variable


# 4. .capitalize() - used to capitalize the first letter of the given string
str.capitalize()
print(str.capitalize())  #will print "Delhiisaverypollutedunionterritory"


# 5. .find(word) - used to find the index of the first letter of the 'word'
str.find("pollute")
print(str.find("pollute"))  #will print the index of 'p' i.e. 12

# 6. .replace(old_word,new_word) - will replace the words
str.replace("polluted","crowded")
print(str.replace("polluted","crowded"))  #will print delhiisaverycrowdedunionterritory