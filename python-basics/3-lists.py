# Lists are like arrays and can hold any of data, and as much of it as wanted.
# They could be iterated against

#We can start with an empty list and append 3 integers and print them by accessing their index location
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])
# We can't access an index that does not exist eg mylist[10]

# We can iterate through the list by accessing each object as x
for x in mylist:
    print(x)

#Exercise
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings = []
strings.append("hello")
strings.append("world")

names = ["John", "Eric", "Jessica"]

second_name = names[1]

# This code writes out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)