a=input("Enter a number between 5 and 9: ")
if a=="quit":
 print("You decided to quit.")
elif int(a)<5 or int(a)>9:
 raise ValueError("Value should be between 5 and 9")