import math

weight = float(input("Please Enter your weight (in kilograms): "))
height = float(input("Please Enter your height (in meter): "))

heigh_t = height ** 2   #BMI = Weight/(Height)^2
BMI = weight / heigh_t
bmi = str(round(BMI, 4))
print(type(bmi))
print("your Body mass index is %i" % BMI)

if BMI < 18.5:
    print("You at underweight situation.")
elif 18.5 < BMI < 24.9:
    print("You at Normal situation.")
elif 25 < BMI < 29.9:
    print("You at overweight situation.")
elif 30 < BMI < 34.9:
    print("You at Obese situation.")
elif BMI > 35:
    print("You at Extremly Overweight situation.")
