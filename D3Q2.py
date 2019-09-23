# Write a method called isLeapYear(someYear) that accepts an integer value (Ex/1904) that represents a year. 
# The method returns the boolean value True if the year is a leap year and False if the year is not.

def isLeapYear(year):
    answer = year % 4
    if(answer == 0):
        print(True)
    else:
        print(False)

number = int(input("Please enter a year "))
isLeapYear(number)