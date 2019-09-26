#Write a program to classify athletes into five weight classes. The program should accept a weight from the user and then print out the appropriate class. The categories are:
#205 - 265 lbs Heavyweight
#185 - 205 lbs Light Heavyweight
#170 - 185 lbs Middleweight
#155 - 170 lbs Welterweight
#145 - 155 lbs Lightweight

def determine_weightclass( weight ):
    if(weight >= 145 and weight <= 155):
        print(f"{weight} lbs is Lightweight")

    elif weight < 170 and weight <= 155:
        print(f"{weight} lbs is Welterweight")

    elif weight < 185 and weight <= 170:
            print(f"{weight} lbs is Middleweight")

    elif weight < 205 and weight <= 185:
        print(f"{weight} lbs is Light Heavyweight")

    else: 
        print (f"{weight} lbs is Heavyweight")
        
#main
w = eval(input("Please enter a weight "))
determine_weightclass(w)