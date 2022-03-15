#Classes
#Objects are an encapsulation of variables and functions into a single entity.
#Objects get their variables and functions from classes.
#Classes are essentially a template to create your objects.

class RandomClass:
    #Class and object name should have the first letter capitalized.
    variable = "meh"
    #^ defining a variable inside of a class

    def function(self):
    #^ defining a function inside of a class
        print("This is a message inside the class.")

newObejectA = RandomClass()
newObejectB = RandomClass()
#^ creating a new object
newObejectA.variable
newObejectB.variable = "Bing Bong"
# ^in order to access a variable inside of an object/class,
# you need to put the object name in front of the variable name.

print(newObejectA.variable)
print(newObejectB.variable)

#You should be able to see that even though they are both a new object of
# RandomClass,they are also different Object

myobjectx.function()
# ^in order to access a function inside of an object/class,
# you need to put the object name in front of the variable name.

class Initiation:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = Initiation(10086)
print(var.returnNumber()) #Prints '10086'

###Exercise
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# Create car1
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00
#^Assign variables value;

# Creae car2
car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00
#^Assign variables value;

# test code
print(car1.description())
print(car2.description())
