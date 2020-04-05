# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def root():

    feet = 0
    inches = 0
    weight = 0

    age = 0
    salary = 0
    savings = 0
    goal = 0

    if request.method == "POST":

        if request.form.get("feet") != "":
            feet = float(request.form.get("feet"))

        if request.form.get("inches") != "":
            inches = float(request.form.get("inches"))

        if request.form.get("weight") != "":
            weight = float(request.form.get("weight"))

        metric_Weight =  weight * 0.45

        metric_Height = ((feet * 12) + inches) * 0.025

        if (metric_Height == 0):
            metric_Height = 1

        bmi = metric_Weight / (metric_Height * metric_Height)

        if (bmi < 18.5):
            category = "Underweight"

        elif ((bmi >= 18.5) and (bmi < 25)):
            category = "Normal"

        elif ((bmi >= 25) and (bmi < 30)):
            category = "Overweight"

        else:
            category = "Obese"


        if request.form.get("age") != "":
            age = float(request.form.get("age"))

        if request.form.get("salary") != "":
            salary = float(request.form.get("salary"))

        if request.form.get("savings") != "":
            savings = float(request.form.get("savings"))

        if request.form.get("goal") != "":
            goal = float(request.form.get("goal"))

        currentSavings = 0
        currentAge = age

        while ((currentSavings <= goal) and (currentAge < 100)):

            savingsThisYr = salary * (savings / 100)
            employerMatch = savingsThisYr * 0.35

            currentSavings = currentSavings + (savingsThisYr + employerMatch)
            currentAge = currentAge + 1

        if (currentAge >= 100):
            message = "You will die before meeting your savings goal..."
        else:
            message = "You will meet your savings goal at " + str(currentAge)

        return render_template('results.html', bmi = bmi, category = category, message = message)
    
    else:

        return render_template('index.html', feet=feet, inches=inches, weight=weight, age=age, salary=salary, savings=savings, goal=goal)



if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)



