# A program that calcultes the body mass index
# formula to calculate body mass index is BMI = kg/m2 where kg
# is a person’s weight in kilograms and m2 is their height in meters squared
# the user to enter his/her weight in kgs and height in cms
# assume the height and weight enterd will be positive integers

print("BMI alculations")

height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kgs: "))

height_meters = height / 100

BMI = weight / (height_meters **2)

print(f"BMI is: {BMI}")

print("You are ", end=" ")

if BMI < 18.5:
    print("Underweight")
elif BMI > 18.4 and BMI <= 24.9:
    print("Normal")
elif BMI > 24.9 and BMI < 30:
    print("Overweight")
else:
    print("Obese. Please Unfat")