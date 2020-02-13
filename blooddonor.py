MIN_AGE = 16
MIN_WEIGHT = 50
Age = int(input("How old are you?"))
Weight = int(input("What is your weight?"))
if Age >= MIN_AGE and Weight >= MIN_WEIGHT:
    print("You are eligible")
else:
    print("You are not eligible")