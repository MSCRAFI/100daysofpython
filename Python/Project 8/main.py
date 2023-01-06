def CtoF(GetNum):
 F = (9/5)*GetNum + 32
 return F
def CtoK(GetNum):
 K = GetNum + 273.15
 return K
def FtoC(GetNum):
 C = (5/9)*(GetNum - 32)
 return C
def FtoK(GetNum):
 K = (5/9)*(GetNum - 32) + 273.15
 return K
def KtoC(GetNum):
 C = GetNum - 273.15
 return C
def KtoF(GetNum):
 F = (9/5)*GetNum - 459.67
 return F
Temp=["Celsius","Fahrenheit","Kelvin"]
inTemp=[int(input("1. Celsius to Fahrenheit\n2. Celsius to Kelvin\n3. Fahrenheit to Celsius\n4. Fahrenheit to Kelvin\n5. Kelvin to Celsius\n6. Kelvin to Fahrenheit\n>> "))]
GetNum=float(input("Enter your Temperature value:- "))
if inTemp[0]==1:
 getValue=CtoF(GetNum)
 print(getValue)
elif inTemp[0]==2:
 getValue=CtoK(GetNum)
 print(getValue)
elif inTemp[0]==3:
 getValue=FtoC(GetNum)
 print(getValue)
elif inTemp[0]==4:
 getValue=FtoK(GetNum)
 print(getValue)
elif inTemp[0]==5:
 getValue=KtoC(GetNum)
 print(getValue)
elif inTemp[0]==6:
 getValue=KtoF(GetNum)
 print(getValue)
else:
 print("Invalid Number. Please check again.")