num1=int(input("Enter your 1st number: "))
condition=input("Enter your condition to complete the math: ")
num2=int(input("Enter your 2nd number: "))
plus=num1 + num2
minus=num1-num2
multiplication=num1*num2
division=num1/num2
if(condition=="+"):
 print("Your addition value is:",plus)
elif(condition=="-"):
 print("Your subtraction value is:",minus)
elif(condition=="*"):
 print("Your multiplication value is:",multiplication)
elif(condition=="/"):
 print("Your division value is:",division)
else:
 print("Your condition is invalid.")