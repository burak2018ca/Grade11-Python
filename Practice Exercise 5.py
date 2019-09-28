# Write a function named isDivisibleBy3( n ) that takes a single integer as a parameter 
# and returns True if the parameter is evenly divisible by 3 and False otherwise.

def isDivisibleBy3 ( n ):
    return (n % 3 == 0)

number = int(input( "Please enter a number "))
print(isDivisibleBy3(number))