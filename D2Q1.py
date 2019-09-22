# Practice Exercises 1

def nameBox (name) :

    nameLength =len(name)

    print ("*" * (nameLength + 2))
    print ("*" + name + "*")
    print("*" * (nameLength + 2))

userName = input("Please enter your name: ")
nameBox(userName)