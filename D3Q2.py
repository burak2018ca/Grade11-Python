# Write a method called isLeapYear(someYear) that accepts an integer value (Ex/1904) that represents a year. 
# The method returns the boolean value True if the year is a leap year and False if the year is not.

def isLeapYear(year):
    if((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))):
        print(True)
    else:
        print(False)

number = int(input("Please enter a year "))
isLeapYear(number)