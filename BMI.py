a=input("Enter Your Name")
print("Welcome to BMI Checking Program ",a)

w=float(input("Enter You Weight(in KG)"))
h=float(input("Enter your height(in CM)"))
h2=h/100
print("Your HEight In Meters Is ; ", h2)
h3=h2*h2
bmi=w/h3
print("Your BMI Is ",bmi)

if bmi<=18.5:
    print("Underweight")
elif bmi >=18 and bmi <=24.9:
    print("Normal Weight")

elif 29.9<=bmi and bmi <=29.9:
    print("Overweight")
else:
    print("obese")    

