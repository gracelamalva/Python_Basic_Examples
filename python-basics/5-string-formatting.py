# Python utilizes C style string formatting to create new, formatted stirngs. The '%' operator can be used to format
# a set of variables enclosed inside a typle or a fixed sized list, with a format string, which contains the tnormal text together
# with 'argument specifiers'; special symbols like %s and %d

# We can have a variable 'name' and print it out like a greeting to a user
name = "John"
print("Hello, %s" % name)

# Use a tuple (parentheses) to use two or more argument specifiers
name = "John"
age = 23
print("%s is %d years old" % (name,age))

# Any object not in a string can be formatted using '%s'
# String returning from the 'repr' method of that object is formatted as the string
mylist = [1,2,3]
print("A list: %s" % mylist)

# Basic Argument specifiers
# %s    String (or any obj with a string representaion, like numbers)
# %d    Integers
# %f    Floating point numbers
# %.<num of digits>f    Floating point numbers with fixed amout of digits to the right of the dot
# %x/%X     Integers in hex representation (lowercase/uppercase)

# Exercise
data = ("John", "Doe", 53.44)
format_string = "Hello"
print("%s %s %s. Your current balance is %f" % (format_string, data[0], data[1], data[2]) )