# Write a function that converts a temperature from Celcius to Fahrenheit
# ( F = ( 9 / 5 ) C + 32 ) ).Your function should accept the temperature as a floating point number
# and print out the converted temperature rounded to the nearest whole number.

def convToFah(cTemp):
    fahrenite = (9 / 5)* cTemp + 32
    return(f"It is {fahrenite} Fahrenite")

celcius = float(34)
print (convToFah(celcius))