# Making Who Wants to Be a Millionaire (WWBM) program

# Using list to add for Qestions
Questions=["1. What is the capital of Bangladesh?\na) Dhaka\nb) Dakar\nc) Dacca\nd) Kolkata\n> ",
"2. What is the capital of France?\na) Dhaka\nb) London\nc) Paris\nd) Rome\n> ",
"3. How long does it take for light to travel from the sun to the earth?\na) 7 Min and 20 Sec\nb) 7 Min and 10 Sec\nc) 8 Min and 20 Sec\nd) 8 Min and 10 Sec\n> ",
"4. How many states are there in the United States?\na) 40\nb) 50\nc) 60\nd) 70\n> ",
"5. What is the largest planet in the solar system?\na) Jupiter\nb) Mars\nc) Earth\nd) Saturn\n> ",
"6. Who is the author of the book \"To Kill a Mockingbird\"?\na) Harper Reed\nb) Lee Child\nc) Lee Smith\nd) Harper Lee\n> ",
"7. How many oceans are there in the world?\na) 4\nb) 5\nc) 6\nd) 7\n> ",
"8. What is the highest mountain in the world?\na) Mount Everest\nb) K2\nc) Mount Kanchenjunga\nd) Mount Lhotse\n> ",
"9. Who was the first president of the United States?\na) James Madison\nb) John Adams\nc) George Washington\nd) Thomas Jefferson\n> ",
"10. How many planets are in the Solar System?\na) 9\nb) 10\nc) 7\nd) 8\n> "]
# Adding all answer on a list
Answers=["a","c","c","b","a","d","b","a","c","d"]
# Getting answer from user and adding it to a list
GetAnswers=[input(Questions[0]),
input(Questions[1]),
input(Questions[2]),
input(Questions[3]),
input(Questions[4]),
input(Questions[5]),
input(Questions[6]),
input(Questions[7]),
input(Questions[8]),
input(Questions[9])]
# Match answer from user generated answer and default answer and add the boolean value to the list
GetBool=[bool(GetAnswers[0]==Answers[0]),
bool(GetAnswers[1]==Answers[1]),
bool(GetAnswers[2]==Answers[2]),
bool(GetAnswers[3]==Answers[3]),
bool(GetAnswers[4]==Answers[4]),
bool(GetAnswers[5]==Answers[5]),
bool(GetAnswers[6]==Answers[6]),
bool(GetAnswers[7]==Answers[7]),
bool(GetAnswers[8]==Answers[8]),
bool(GetAnswers[9]==Answers[9])]
# Count boolean value in the list
CountBool=GetBool.count(True)
# Multiply total True boolean in the list with 100000 to get Prize Value
TotalPrizeWin= CountBool*100000
# Using if else for printing the end value
if 100000<TotalPrizeWin<1000000:
 print("Congratulations, You've won", TotalPrizeWin, "USD.")
elif TotalPrizeWin==1000000:
 print("Congratulations, You've won the grand prize of 1 Million USD.")
else:
 print("Sorry to say but you didn't win anything. Here we have this consolation prize for you. Hope you get better luck next time.")
