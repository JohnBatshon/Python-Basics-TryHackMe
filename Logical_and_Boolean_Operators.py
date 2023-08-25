
# Logical operators allow assignment and comparisons to be made and are used in conditional testing (such as if statements).

# Logical Operation         | Operator  | Example
# Equivalence	            | ==	    | if x == 5
# Less than	                | <	        | if x < 5
# Less than or equal to     | <=	    | if x <= 5
# Greater than	            | >	        | if x > 5
# Greater than or equal to  | >=	    | if x >= 5

# Boolean operators are used to connect and compare relationships between statements.
# Like an if statement, conditions can be true or false.

# Boolean Operation	Operator Example
# Both conditions must be true for the statement to be true	AND
# if x >= 5 AND x <= 100
# Returns TRUE if x is
# a number between 5 and 100
# Only one condition of the statement needs to be true 	OR
# if x == 1 OR x == 10
# Returns TRUE if X is 1 or 10
# If a condition is the opposite of an argument	NOT
# if NOT y
# Returns TRUE if the y value is False

# Example #1:

a = 1
if a == 1 or a > 10:
     print("a is either 1 or above 10")

# Example # 2:

name = "bob"
hungry = True
if name == "bob" and hungry == True:
     print("bob is hungry")
elif name == "bob" and not hungry:
     print("Bob is not hungry")
else: # If all other if conditions are not met
     print("Not sure who this is or if they are hungry") 

