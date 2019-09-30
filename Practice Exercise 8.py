#Driving Age
#Traffic rules are as follows:
#Under 18, must have a G1 permit.
#Between 18 and 70, must have a G permit.
#Over the age of 70, must have a G permit and updated yearly test.
class Driver:
  def __init__(self, age, licenceType, yearlyTest):
      self.age = age
      self.licenceType = licenceType
      self.yearlyTest = yearlyTest
    
  def driverLicence(self):
    print(f"Driver Licence\n{self.age} \n{self.licenceType} \n{self.yearlyTest}\n")

  def licenseCheck(self):
    if(self.age <= 18 and (self.licenceType == "G1" or self.licenceType == "G")):
        print("You are allowed to drive")
    elif(self.age < 70 and self.age > 18  and self.licenceType == "G"):
        print("you are allowed to drive")
    elif(self.age >= 70 and self.licenceType == "G" and self.yearlyTest == "Yes"):
        print("you are allowed to drive") 
    else:
        print("Sir! Please step out of the car")

d1 = Driver(35, "G1", "no")
d1.driverLicence()
d1.licenseCheck()