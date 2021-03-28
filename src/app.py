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
    feet = int(request.form['feet'])
    inches = int(request.form['inches'])
    pounds = float(request.form['pounds'])

    ##what if they entered strings?

    if (feet * 12 + inches <= 0):
        return render_template('app.html',bmi="Your total height must be greater than 0")
    elif (pounds <= 0):
        return render_template('app.html',bmi="Surely you weight something")
    elif ((feet * 12 + inches > 0) and pounds > 0):
        return render_template('app.html',bmi=("%.3f" % Functions.getBMI(feet,inches,pounds)) + " BMI")
    else:
        return render_template('app.html',bmi="")

@app.route('/getretirementage',methods=["POST"])
def sendRetAge():
    #pull data
    age = float(request.form['age'])
    anualSalary = float(request.form['anualSalary'])
    percentSasved = float(request.form['percentSasved'])
    desiredSavings = float(request.form['desiredSavings'])

    #validate input here

    return render_template('app.html',retirementAge="null still working")
 
app.run(debug = True, host='localhost', port=5000)