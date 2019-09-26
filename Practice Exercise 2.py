# Write a main for the function called compare ( x, y ) shown below.

def compare (x,y):
     if x < y:
          print (f'{x} is less than {y}')

     elif x > y:
          print (f'{x} is greater than {y}')

     else:
          print (f' {x} and {y} are equal')

number1 = int(input("Please enter the first number "))
number2 = int(input("Please enter the second number "))

compare(number1, number2)