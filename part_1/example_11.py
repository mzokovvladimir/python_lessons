weight = float(input("Input your weight in kg: "))
height = float(input("Input your height in m: "))
imt = weight / (height ** 2)
category = "Underweight" if imt < 18.5 else "Norm" if imt < 24.9 else "Overweight" if imt < 29.9 else "Obesity"
print(f"Your imt: {imt:.2f}. category: {category}")
