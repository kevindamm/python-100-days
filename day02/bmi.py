# For the record, I don't think BMI is a useful metric.  At best it is a rough
# approximation with usefulness limited to extreme values.

height = float(input("enter your height in meters: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / (height ** 2)

print(f"Your BMI is {bmi}. kthxbai")