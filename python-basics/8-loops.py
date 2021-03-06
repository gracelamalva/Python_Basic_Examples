#Loops: There are two types of loops in Python, for and while.
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

#For loops can iterate over a sequence of numbers using the "range" and "xrange" functions. 
#The difference between range and xrange is that the range function returns a new list with numbers of that specified range, whereas xrange returns an iterator, which is more efficient.
# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

#While loops repeat as long as a certain boolean condition is met. For example:
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

#break is used to exit a for loop or a while loop, whereas continue is used to skip the current block, and return to the "for" or "while" statement. 
# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

#When the loop condition of "for" or "while" statement fails then code part in "else" is executed. If a break statement is executed inside the for loop then the "else" part is skipped.
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

#Exercise
#Loop through and print out all even numbers from the numbers list in the same order they are received. Don't print any numbers that come after 237 in the sequence.
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

for x in numbers:
    if x == 237:
        print(x)
        break;
    elif x % 2 == 0:
        print(x)
	