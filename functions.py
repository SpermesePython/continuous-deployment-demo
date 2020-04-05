def calc_BMI(feet, inches, weight):
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

    bmi = truncate(bmi, 1)

    return bmi, category

def calc_RA(age, salary, savings, goal):
    currentSavings = 0
    currentAge = age

    while ((currentSavings <= goal) and (currentAge < 100)):

        savingsThisYr = salary * (savings / 100)
        employerMatch = savingsThisYr * 0.35

        currentSavings = currentSavings + (savingsThisYr + employerMatch)
        currentAge = currentAge + 1

    currentAge = truncate(currentAge)

    if (currentAge >= 100):
        message = "You will die before meeting your savings goal..."
    else:
        message = "You will meet your savings goal at " + str(currentAge)

    return message
