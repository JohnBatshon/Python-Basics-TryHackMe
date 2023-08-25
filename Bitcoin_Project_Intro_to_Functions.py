

# Example Function

def sayHello(name):
     print("Hello " + name + "! Nice to meet you.")

sayHello("ben") # Output is: Hello Ben! Nice to meet you

# There are some key components we can note from this function:

# The def keyword indicates the beginning of a function. The function is followed by a name that the programmer defines (and is a function parameter). In our example, it's sayHello.
# Following the function name is a pair of parenthesis () that holds input values, data that we can pass into the function. In our example, it's a name.
# A colon : marks the end of the function header.

# Function returning a Result Example:

def calcCost(item):
     if(item == "sweets"):
          return 3.99
     elif (item == "oranges"):
          return 1.99
     else:
          return 0.99

spent = 10
spent = spent + calcCost("sweets")
print("You have spent:" + str(spent))

# If we call the calcCost function and pass in "sweets" as the item parameter, the function will return a decimal number (float). In the code above, we take a variable called spent and add the cost of "sweets" through the calcCost function; when we call calcCost, it will return the number 3.99.

investment_in_bitcoin = 1.2
bitcoin_to_usd = 40000

# 1) write a function to calculate bitcoin to usd
# 2) use function to calculate if the investment is below $30,000
# 3) use function to calculate if its below $30,000

def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
  usd_value = investment_in_bitcoin * bitcoin_to_usd
  return usd_value

my_bitcoin_value = bitcoinToUSD(investment_in_bitcoin, bitcoin_to_usd)
if my_bitcoin_value <= 30000:
  print("Your bitcoin is worth less than 30000")
else:
  print("Your bitcoin is worth more than 30000")