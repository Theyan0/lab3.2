def bmi_calculator(weight,height):
    bmi = weight / height ** 2
    if bmi < 18.5:
        num1 = -1
        return (num1)
    elif bmi > 25.0:
        num2 = 1
        return (num2)
    else:
        num3 = 0
        return (num3)
    return(bmi)

height = float(input("Your height:"))
weight = float(input("Your weight:"))
bmi = bmi_calculator(weight,height)
print("your bmi:"+str(bmi))