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
    if (not feet.isdigit):
        return render_template('app.html',bmi="Your feet value must be a number")
    elif (not inches.isdigit):
        return render_template('app.html',bmi="Your inches value must be a number")
    elif (not pounds.isdigit):
        return render_template('app.html',bmi="Your pounds value must be a number")
    
    #cast to data types
    feet = int(feet)
    inches = int(inches)
    pounds = float(pounds)

    #proper number validation
    if (feet * 12 + inches <= 0):
        return render_template('app.html',bmi="Your total height must be greater than 0")
    elif (pounds <= 0):
        return render_template('app.html',bmi="Surely you weight something")
    elif ((feet * 12 + inches > 0) and pounds > 0):
        return render_template('app.html',bmi=
        ("%.3f" % Functions.getBMI(feet,inches,pounds)) + " BMI")
    else:
        return render_template('app.html',bmi="")

@app.route('/getretirementage',methods=["POST"])
def sendRetAge():
    #pull data
    age = str(request.form['age'])
    anualSalary = str(request.form['anualSalary'])
    percentSasved = str(request.form['percentSasved'])
    desiredSavings = str(request.form['desiredSavings'])

    #what if they entered strings?
    if (not age.isdigit):
        return render_template('app.html',bmi="Your age value must be a number")
    elif (not anualSalary.isdigit):
        return render_template('app.html',bmi="Your salary value must be a number")
    elif (not percentSasved.isdigit):
        return render_template('app.html',bmi="Your percetn saved value must be a number")
    elif (not desiredSavings.isdigit):
        return render_template('app.html',bmi="Your desired savings value must be a number")

    #cast to data types
    age = float(age)
    anualSalary = float(anualSalary)
    percentSasved = float(percentSasved)
    desiredSavings = float(desiredSavings)

    #make sure things that need to be greater than 0 are and if so, return calculation and category

    return render_template('app.html',retirementAge="null still working")
 
app.run(debug = True, host='localhost', port=5000)