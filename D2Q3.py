# Write a function that converts a temperature from Celcius to Fahrenheit
# ( F = ( 9 / 5 ) C + 32 ) ).Your function should accept the temperature as a floating point number
# and print out the converted temperature rounded to the nearest whole number.

def convToFah(cTemp):
    Fahrenite = (9 / 5)* cTemp + 32
    print(f"It is {Fahrenite} Fahrenite")

celcius = float(input("Please enter the tempreture in celcius "))
convToFah(celcius)