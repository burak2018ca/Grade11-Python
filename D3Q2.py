#Write a function called isEven(number) that returns True if the number is even and False if the number isn't.
def isEven(num):
    return num % 2 == 0

userNum = int(input("Please enter a number: "))
print(isEven(userNum))