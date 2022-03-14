# Strings are bits of text that can be defined as anything between quotes
astring = "Hello world!"
atring2 = 'Hello world!'

# We can use single quotes to assign a string, but we will face problems if we store the value to be assigned itself contains single quotes
# We can fix this by surrounding them in double quotes
astring  = "Hello world!"
print("single quotes are ' ' ")
print(len(astring))

#.index(char) wil print out 4 because the index location of the first occurence of 'o' is 4 chars away from the first char.
# There are two o's but this method will recognize the first
astring = "Hello world!"
print(astring.index("o"))

#.count(char) counts the number of l's in the string, and should print out 3
astring = "Hello world!"
print(astring.count("l"))

# We can print a slice of a string starting at an index and ending up to but not including another index.
# If there is only one number, it will give a single char at that index.
# If you leave out the first number, but keep colon, it will give you a slie from the start to the number you left.
# If you leave out the second number, it will give a slice from the first number to the end.
# We can include negative numbers in the brackets, and are an easy way of starting at the end of the string instead of the beginning.
# eg: -3 = 3rd char from the end
# This prints the characters from 3 to 7 skipping 2 chars, aka extended slice syntax; form = [start:stop:step]
astring = "Hello world!"
print(astring[3:7:2])
print(astring[3:7:1])

# We can reverse a string
print(astring[::-1])

# We can convert strings with all letters to uppercase and lowercase
print(astring.upper())
print(astring.lower())

#We can determine whether a string starts with something, or ends with something
# It will retun true or false depending on the situation
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdfadf"))

# Strings can be split into a group of strings together in a list.
# We can split at a space
afewwords = astring.split(" ")
print(afewwords)




#Exercise
s = "Hey! should this be?"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
s= "Hi here a"
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
s = "Here are some a's in this sentence"
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

s = "Stronger"
# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

s = "Handsome!"
# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
s = "Some new words to split up"
print("Split the words of the string: %s" % s.split(" "))


