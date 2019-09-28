#Write a function named calculatePayroll(hoursWorked, hourlyRate) that takes two parameters. 
# The function should calculate and return the amount paid to employee. 
# The function should also handle when an employee works overtime. 
# Overtime hours are paid at 1.5 times the hourlyRate.

#Example/ Shelley works 46 hours and earns $8.75 an hour.
#She earns 40 * 8.75 (regular) + 6 * 13.13 (overtime) = $428.78

def calculatePayroll( hoursWorked, hourlyRate ):
    if(hoursWorked > 40):
        overtime = hoursWorked - 40
        regularTime = hoursWorked - overtime
        return((regularTime * hourlyRate) + (overtime * (hourlyRate * 1.5)) )
    else:
        return(hoursWorked * hourlyRate)

hours = eval(input("Please enter total hours worked for week "))
rate = eval(input("Enter the hourly rate "))
print(calculatePayroll(hours, rate))