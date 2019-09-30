# 100-199 is Philosophy
# 200-299 is Religion
# 300-399 is Social Science
# 400-499 is Language
# 500-599 is Pure Science
# 600-699 is Technology
# 700-799 is Arts
# 800-899 is Literature
# 900-999 is History

def library ( bookNumber):
    if(bookNumber >= 100 and bookNumber < 200):
        return(f"Your book is in the Philosophy Section")
    elif(bookNumber >= 200 and bookNumber < 300):
        return(f"Your book is in the Religion Section")
    elif(bookNumber >= 300 and bookNumber < 400):
        return(f"Your book is in the Social Science Section")
    elif(bookNumber >= 400 and bookNumber < 500):
        return(f"Your book is in the Language Section")
    elif(bookNumber >= 500 and bookNumber < 600):
        return(f"Your book is in the Pure Science Section")
    elif(bookNumber >= 600 and bookNumber < 700):
        return(f"Your book is in the Technology Section")
    elif(bookNumber >= 700 and bookNumber < 800):
        return(f"Your book is in the Arts Section")
    elif(bookNumber >= 800 and bookNumber < 900):
        return(f"Your book is in the Literature Section")
    elif(bookNumber >= 900 and bookNumber < 100):
        return(f"Your book is in the History Section")

answer= int(input("Please enter the book number "))

print(library(answer))