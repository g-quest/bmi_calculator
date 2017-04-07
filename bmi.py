unitType = input("Let's compute your BMI! \n\nWould you like to use metric \
units or imperial units? \nEnter 1 for metric, 0 for imperial: ")

METRIC = "1"
IMPERIAL = "0"

# user chooses metric
if unitType == METRIC:
    metricWeight = float(input("Enter weight in kilograms: "))
    metricHeight = float(input("Enter height in meters: "))

    # BMI formula: kilograms/meters^2
    BMI = metricWeight/metricHeight**2

    print("\nYour BMI is {:.2f}!".format(BMI))
 
#user chooses imperial 
else:
    poundsWeight = float(input("Enter weight in pounds: "))
    inchesHeight = float(input("Enter height in inches: "))

    # pounds to kilograms: 1 pound = 0.453592 kilograms
    weightToMetric = poundsWeight*0.453592

    # inches to meters: 1 inch = 0.0254 meters
    inchesToMetric = inchesHeight*0.0254

    # BMI is computed in metric
    convertedBMI = weightToMetric/inchesToMetric**2

    # display BMI in metric
    print("\nYour BMI is {:.2f}!".format(convertedBMI)) 
