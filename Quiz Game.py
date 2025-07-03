questions = ("What is the capital of Pakistan?",
             "Who is the no 10 of Argentina?",
             "Which era of football was considered as the gratest?",
             "Which sport is the number #1 in the world?",
             "Which department of IST is best?")
options = (("A.Karachi", "B. Peshawer", "C. Islamabad", "D. lahore"),
           ("A.Messi", "B. Di Maria", "C. Mac Allister", "D. Almada"),
           ("A. 20s", "B. 10s", "C. 00s", "D. 90s"),
           ("A. Basketball", "B. Football", "C. Cricket", "D. Tennis"),
           ("A. CS", "B. Aero", "C. Avi", "D. Mechanical"))
answers = ("C", "A", "B", "B", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is correct")
    question_num += 1

print("-------------------------------")
print("           RESULT              ")
print("-------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score/ len(questions) * 100)
print(f"Your score is {score} %")