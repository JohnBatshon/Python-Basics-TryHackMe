# In programming, loops allow programs to iterate and perform actions a number of times. There are two types of loops, for and while loops.

# While Loop Example:

i = 1
while i <= 10:
     print(i)
     i = i + 1

# This while loop will run 10 times, outputting the value of the i variable each time it iterates (loops). Let's break this down:

# The i variable is set to 1
# The while statement specifies where the start of the loop should begin
# Every time it loops, it will start at the top (outputting the value of i)
# Then it goes to the next line in the loop, which increases the value of i by 1
# Then (as there is no more code for the program to execute), it goes to the top of the loop, starting the process over again
# The program will keep on looping until the value of the i variable is greater than 10

# For Loops

# A for loop is used to iterate over a sequence such as a list. 
# Lists are used to store multiple items in a single variable, and are created using square brackets.

# For Loops Example:

websites = ["facebook.com", "google.com", "amazon.com"]
for site in websites:
     print(site)

# This for loop shown in the code block above, will run 3 times, outputting each website in the list. Let's break this down:

# The list variable called websites is storing 3 elements
# The loop iterates through each element, printing out the element
# The program stops looping when it's been through each element in the loop

# Below is some example Python code that will print the numbers from 0 to 4. In programming, 0 is often the starting number, so counting to 5 is 0 to 4 (but has 5 numbers: 0, 1, 2, 3, and 4)

for i in range(5):
     print(i)

# To print 0-50 the range would end at 51 in the example below.

# for i in range(51):
#  print(i)