import Functions

def mainWeb():
    return 0

def mainCLI():
    while True:
        print("Enter your choice:\n(1) Body Mass Index Calculator\n(2) Retirement Age Calculator\n(3) exit")
        userInput = input(">> ")
        print()

        if (userInput not in ["1","2","3"]):
            print("Invalid option, must enter 1,2, or 3")
            continue
        
        if (userInput == "1"):
            feet = 0
            while True:
                print("Enter your height in feet (inches are next)")
                feet = input(">> ")
                feet = float(feet)
                if (isinstance(feet, float) and feet >= 0):
                    break
                else:
                    print("Your feet value must be a positive number")
                    continue

            inches = 0
            while True:
                print("Enter your inches measurement (should be less than 12)")
                inches = input(">> ")
                inches = float(inches)
                if (isinstance(inches, float) and inches >= 0):
                    break
                else:
                    print("Your inches value must be a positive number")
                    continue
            while inches >= 12:
                inches -= 12
                feet += 1

            pounds = 0
            while True:
                print("Enter your weight in pounds")
                pounds = input(">> ")
                pounds = float(pounds)
                if (isinstance(pounds, float) and pounds > 0):
                    break
                else:
                    print("Your pounds value must be a positive number")
                    continue
            bmi = Functions.getBMI(feet,inches,pounds)
            print("Your BMI is ", end = '')
            print("%.3f" % bmi, end = '')
            print(" (",Functions.getBMICategory(bmi),")")

        elif (userInput == "2"):
            break #todo implement me still for complete CLI and web app

        elif (userInput == "3"):
            print("Exiting program")
            break
    
mainCLI()