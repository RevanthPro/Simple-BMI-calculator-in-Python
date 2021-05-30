#Taking Input from the user
name = input("Hi, What's your name?")
height = float(input("What's your height? (In metres)"))
weight = float(input("What's your weight? (In kg)"))

#Our next task is to identify the BMI of the user. BMI's formula is (kg/metres squared)

#Converting the value of our user's height from metres to metres squared
height = height * height # or height ** 2 (aka) height to the power of 2

#Calculating the BMI
BMI = weight/height

#Knowing if the person is overweight or underweight or normal weight
'''
If the person's BMI is below 18.5 then he is underweight
Or if the person's BMI is between 18.5 and 24.9 then the person's BMI is normal
Or if the person's BMI is above 24.9 then the person is overweight'''

#Coding if statements
if BMI < 18.5:
    print(name + " is underweight")
elif BMI <= 24.9:
    print(name + " is normal")
else:
    print(name + " is overweight")