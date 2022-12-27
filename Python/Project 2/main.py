import time
timestamp= time.strftime("%I:%M:%S %p")
Hour24=int(time.strftime("%H"))
Name=input("Please Enter Your Name: ")
print(timestamp)
if(Hour24<5):
 print(Name,"Please sleep. This is mid night.")
elif(5<=Hour24<7):
 print(Name,"This is early morning. You can wake up and do some light exercise.")
elif(7<=Hour24<12):
 print("Good Morning," ,Name)
elif(12<=Hour24<15):
 print("Good Day," ,Name)
elif(15<=Hour24<18):
 print("Good Afternoon," ,Name)
elif(18<=Hour24<21):
 print("Good Evening," ,Name)
elif(21<=Hour24<24):
 print("Good Night," ,Name,"Sweet Dreams.")
else:
 print("Invalid Time.")