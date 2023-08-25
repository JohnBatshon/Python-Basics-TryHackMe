# Using "if statements" allows programs to make decisions. They let a program chose a decision based on a condition. Below is an example of how an if statement can be used to determine the section of code (which print statement) to use.

#Example: 

# age = 12
age = 30
if age < 17:
    print('You are NOT old enough to drive')
else:
    print('You are old enough to drive')

# In the example, if you are younger than 17, the program will output the text "You are NOT old enough to drive"; however, if you are over the age of 17, the program will output "You are old enough to drive". Depending on a condition (in this example, it's the age variable), the program will run different code sections.

# There are some key components we note from our code example above:

# The if keyword indicates the beginning of the if statement, followed by a set of conditions.
# The if statement is only run if the condition (or sets of conditions) is true. In our example, it's age < 17; if that condition is true (age is below 17), the code within the if statement runs. Per the example, if certain conditions are not met, the program can default to running code shown in the else part of the if statement. 
# A colon : marks the end of the if statement.
# Note the indentation. Anything after the colon that is indented, is considered part of the if statement, which the program will execute.


# shipping.py challenge

"""
    In this project, you'll create a program that calculates the total
    cost of a customers shopping basket, including shipping.

    - If a customer spends over $100, they get free shipping
    - If a customer spends < $100, the shipping cost is $1.20 per kg of the baskets weight

    Print the customers total basket cost (including shipping) to complete this exercise.

"""

#customer_basket_cost = 34
#customer_basket_weight = 44

# Write if statement here to calculate the total cost

customer_basket_cost = 34
customer_basket_weight = 44
shipping_cost = 1.20
shipping = shipping_cost * customer_basket_weight
total = shipping + customer_basket_cost
# Write if statement here to calculate the total cost

if customer_basket_cost > 100:
  print ("You get free shipping!")
else:
  shipping = customer_basket_weight * 1.20
  print ("Your shipping cost is:")
  print (total)