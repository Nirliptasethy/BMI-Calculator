# BMI Calculator Project
print("===== BMI Calculator ==== ")
while(True):
    try:
        # users input
        weight=float(input("enter your weight in kg :"))
        height=float(input("enter your height in m :"))
        if (weight<=0 or height<=0):
            print("don't enter negative value for weight snd height and try again......")
        else:
            # calculate BMI
            BMI=weight/(height**2)
            # classify BMI into catagory
            if BMI<18.5:
                catagory="Underweight"
            elif BMI<25:
                catagory="Normal"
            elif BMI<30:
                catagory="Overweight"
            else :
                catagory="Obese"
            print("---------------------------")
            print("\n BMI :",round(BMI,2))
            print("\ncatagory:",catagory)

    except ValueError:
        print("Don't try to enter alpnums, strs and symbols ...invalid input and try again....")