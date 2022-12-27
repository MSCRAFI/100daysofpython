marks=[7,15,17,32,34,41,69,75,88,95]
GetMarks= marks[int(input("Enter index number of marks: "))]
if GetMarks>=33:
 if GetMarks>=60:
  if GetMarks>=70:
   if GetMarks>=80:
    if GetMarks>=90:
     if GetMarks>=100:
      print("Perfect.")
     else:
      print("You've done a great job. You're close to getting a perfect result.")
    else:
     print("You've worked hard and the result showed it. keep it up.")
   else:
    print("Your hard work is showing results. Keep doing it you'll do much better next time.")
  else:
   print("I can see you're trying. Try a little more harder next time.")
 else:
  print("You're passed but you need to try a lot harder.")
else:
 print("I'm sorry to say but you've failed.")
