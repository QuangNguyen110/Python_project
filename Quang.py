questions = ("What is The capital of Canada?",
             "What is the square root of 144?",
             "What is the fastest land animal?",
             "What is the chemical symbol for Gold?",
             "How many continents are there on Earth?")

options = (("A. Toronto", "B. Vancouver", "C. Montreal", "D. Ottawa"),
           ("A. 10", "B. 11", "C. 12", "D. 13"),
           ("A. Cheetah", "B. Horse", "C. Ostrich", "D. Chameleon"),
           ("A. Ag", "B. Au", "C. At", "D. Br"),
           ("A. 6", "B. 7", "C. 8", "D. 9"))

answer = ("D","C","A","B","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter your answer: ").upper()
    guesses.append(guess)
    if guess == answer[question_num]:
        score += 1
        print("CORRECT!!")
    else:
        print("INCORRECT!!")
    question_num += 1

score = int(score / len(questions) * 100)

print("------  RESULTS  -----")
print(answer)
print(f"Your score is : {score}%")