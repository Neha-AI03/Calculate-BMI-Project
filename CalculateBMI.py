def calculate_bmi(weight, height):
    bmi=weight/(height**2)
    print(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")
#Example usage
weight=float(input("Enter your weight(kg): "))
height=float(input("Enter your height(m): "))
calculate_bmi(weight,height)
