import math as m
import sys

def getRetirementAge(age, anualSalary, percentSaved, desiredSavings):
    if ((anualSalary == 0 or percentSaved == 0) and desiredSavings != 0):
        return sys.maxsize;
    elif (desiredSavings == 0):
        return age;
    else:
        return m.ceil((desiredSavings / (1.35 * percentSaved / 100.0 * anualSalary)) + age)

def getRetirementCategory(retAge):
    return "will not meet" if retAge >= 100.0 else "will meet"

def getBMI(feet, inches, pounds):
    if ((feet + inches) == 0):
        return sys.maxsize
    elif (pounds == 0):
        return 0
    else:
        pounds *= 0.45
        inches += feet * 12
        inches *= 0.025
        inches *= inches
        return pounds/inches

def getBMICategory(BMI):
    if (BMI < 18.5):
        return "underweight"
    elif (BMI >= 18.5 and BMI < 25.0):
        return "normal"
    elif (BMI >= 25.0 and BMI < 30.0):
        return "overweight"
    else:
        return "obese"