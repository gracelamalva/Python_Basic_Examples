#Defining an integer number
myint = 9
print('Int num: ', myint)

#Defining a floating number
myfloat = 2.0
print('Float num: ',  myfloat)

myfloat = float(7)
print('Float num: ' , myfloat)

#Defining strings with single or double quotes
mystring = 'hello'
print('String from single quote: ' , mystring)
mystring = "hello"
print('String from double quote: ' , mystring)
mystring = "Don't worry with apostrophes with double quotes, but worry about them with single quotes."
print (mystring)

#Operators can be used on numbers and strings
one = 1
two = 2
three = one + two
print("One plus two is: " , three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print("Hello and world is: ", helloworld)

#We can assign more than one variale simultaneously on th same line
#We can not mix operators between numbers and stings 
a,b = 3,4
print(a, b)

#Exercise
mystring = "hello"
myfloat = 10.0
myint = 20
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)




