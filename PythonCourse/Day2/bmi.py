#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# bmi = weight / (height)^2


height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / (float(height) * float(height))

bmi = float(weight) / (float(height) ** 2)

print(int(bmi))