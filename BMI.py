def cal(w,h):
    h2 = h/100  
    print("Your HEight In Meters Is ; ", h2)
    h3=h2*h2
    bmi=w/h3
    return bmi

def bmi_value(bmi):
    if bmi<=18.5:
        print("You Are Underweight")
    elif bmi >=18 and bmi <=24.9:
        print("You Are Normal Weight")

    elif 29.9<=bmi and bmi <=29.9:
        print("You Are Overweight")
    else:
        print("OBESE")    


a=input("Enter Your Name")
print("Welcome to BMI Checking Program ",a)
w=float(input("Enter You Weight(in KG)"))
h=float(input("Enter your height(in CM)"))
bmi= cal(w,h)
print(bmi)
bmi_value(bmi)
