from flask import Flask,render_template,request, request
import Functions
 
app = Flask(__name__)
 
@app.route('/')
def main():
    return render_template('app.html')

#submit bmi
@app.route('/getbmi',methods=["POST"])
def send():
    #pull data
    feet = str(request.form['feet'])
    inches = str(request.form['inches'])
    pounds = str(request.form['pounds']) 

    #what if they entered strings?
    if (not feet.isdigit()):
        return render_template('app.html',bmi="Your feet value must be an integer",feet = feet, inches = inches, pounds = pounds)
    elif (not inches.isdigit()):
        return render_template('app.html',bmi="Your inches value must be an integer",feet = feet, inches = inches, pounds = pounds)
    elif (not pounds.isdigit()):
        return render_template('app.html',bmi="Your pounds value must be an integer",feet = feet, inches = inches, pounds = pounds)
    
    #cast to data types
    feet = int(feet)
    inches = int(inches)
    pounds = int(pounds)

    #proper number validation
    if (feet * 12 + inches <= 0):
        return render_template('app.html',bmi="Your total height must be greater than 0",feet = feet, inches = inches, pounds = pounds)
    elif (pounds <= 0):
        return render_template('app.html',bmi="Surely you weight something",feet = feet, inches = inches, pounds = pounds)
    elif ((feet * 12 + inches > 0) and pounds > 0):
        return render_template('app.html',bmi=
        ("%.3f" % Functions.getBMI(feet,inches,pounds)) 
        + " (" + Functions.getBMICategory(Functions.getBMI(feet,inches,pounds)) + ")")
    else:
        return render_template('app.html',bmi="",feet = feet, inches = inches, pounds = int(pounds))

#todo when calculating result, don't remove field values
#when a field value is wrong, don't remove everything either
@app.route('/getretirementage',methods=["POST"])
def sendRetAge():
    #pull data
    age = str(request.form['age'])
    anualSalary = str(request.form['anualSalary'])
    percentSasved = str(request.form['percentSasved'])
    desiredSavings = str(request.form['desiredSavings'])

    #what if they entered strings?
    if (not age.isdigit()):
        return render_template('app.html',retirementAge="Your age value must be an integer", age = age, anualSalary = anualSalary, percentSasved = percentSasved, desiredSavings = desiredSavings)
    elif (not anualSalary.isdigit()):
        return render_template('app.html',retirementAge="Your salary value must be an integer", age = age, anualSalary = anualSalary, percentSasved = percentSasved, desiredSavings = desiredSavings)
    elif (not percentSasved.isdigit()):
        return render_template('app.html',retirementAge="Your percent saved value must be an integer", age = age, anualSalary = anualSalary, percentSasved = percentSasved, desiredSavings = desiredSavings)
    elif (not desiredSavings.isdigit()):
        return render_template('app.html',retirementAge="Your desired savings value must be an integer", age = age, anualSalary = anualSalary, percentSasved = percentSasved, desiredSavings = desiredSavings)

    #cast to data types
    age = float(age)
    anualSalary = float(anualSalary)
    percentSasved = float(percentSasved)
    desiredSavings = float(desiredSavings)

    if (age <= 0):
        return render_template('app.html',retirementAge="I'm pretty sure you're at least 12 years old", age = age, anualSalary = anualSalary, percentSasved = percentSasved, desiredSavings = desiredSavings)
    elif (anualSalary <= 0):
        return render_template('app.html',retirementAge="If you don't make any money, then I can't do much for you")
    elif (percentSasved <= 0):
        return render_template('app.html',retirementAge="If you don't plan on saving any money, may God have mercy on your soul")
    elif (desiredSavings <= 0):
        return render_template('app.html',retirementAge="If your desired savings is $0, then you've already hit your goal! Woo Hoo!")
    else:
        return render_template('app.html',retirementAge=
         str(Functions.getRetirementAge(age,anualSalary,percentSasved,desiredSavings))
        + " (" + str(Functions.getRetirementCategory(Functions.getRetirementAge(age,anualSalary,percentSasved,desiredSavings))) + ")")
 
app.run(debug = True, host='localhost', port=5000)