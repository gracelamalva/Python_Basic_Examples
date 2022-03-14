# Operators include  the addition, subtraction, multiplication, and division operators, which can be used with numbers.
number = 1 + 2 * 3 / 4.0
print(number)

# The modulo operator returns the integer remainder of the division; dividend % divisor = remaider
remainder = 11 % 3 
print(remainder)

# Two multiplication symbols makes a power relationship
squared = 7**2
cubed = 2 **3 
print(f'Squared', {squared})
print(cubed)

# We can use operators with strings, concatenating them with the addition operator
helloworld = "hello" + " " + "world"
print(helloworld)

#We can multiply strings to form a repeating sequence
lotsofhellos = "hello" * 10
print(lotsofhellos)

# Lists can be joined with the addition operators
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# Like strings, we could format new lists with a repeating sequence using the multiplication operator
print([1,2,3] * 3)

# Exercise
x = object()
y = object()

x_list = []
y_list = []
for i in range(10):
    x_list.append(x)
    y_list.append(y)

big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

