#Conditions

#Python uses boolean logic to evaluate conditions. The boolean values True and False are returned when an expression is compared or evaluated.
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

# Boolean operators: The "and" and "or" boolean operators allow building complex boolean expressions. 
name = "Daquan"
age = 75
if name == "Daquan" and age == 75:
    print("Your name is Daquan, and you are also 75 years old.")

if name == "Daquan" or name == "Gainz":
    print("Your name is either Daquan or Gainz.")

#The "in" operator: could be used to check if a specified object exists within an iterable object container.
name = "Matt"
if name in ["Matt", "Joe"]:
    print("Your name is either Matt or Joe.")

#Python uses indentation to define code blocks, instead of brackets. The standard Python indentation is 4 spaces, although tabs and any other space size will work, as long as it is consistent. Notice that code blocks do not need any termination.
tacos = 10
if tacos == 2:
    print("x equals ten!")
else:
    print("x does not equal to ten.")

#The "is" operator does not match the values of the variables, but the instances themselves.
amigo = [97,98,99]
amiga = [97,98,99]
print(amigo == amiga) # Prints out True
print(amigo is amiga) # Prints out False

#The "not" before a boolean expression inverts it.
print(not False) # Prints out True
print((not False) == (False)) # Prints out False

#Exercise: Change the variables in the first section, so that each if statement resolves as True.
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")