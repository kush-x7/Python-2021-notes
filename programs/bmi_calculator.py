#1. Create a greeting for your program.
print("Welcome to the BMI calculator")

#2. Ask user to input his/her height
height = input("enter your height in m: ")
weight = input ("enter your weight in  kg: ")

#3. Convert the input string into integer / float
weight_int =int(weight)
height_float = float(height)

#4. Calculate BMI
bmi =  weight_int /height_float **2
bmi_as_int = int(bmi)

#5. Print the result
print ( f"Your body mass index is: {bmi_as_int}" )
