# Compound interest

questions = ("Aa?",
             "Bb?",
             "Cc?",
             "Dd?",
             "Ee?")

options = (("A. 110", "B. 220", "C. 330", "D. 440"),
           ("A. 111", "B. 222", "C. 333", "D. 444"),
           ("A. 112", "B. 223", "C. 334", "D. 445"),
           ("A. 113", "B. 224", "C. 335", "D. 446"),
           ("A. 1111", "B. 2222", "C. 3333", "D. 4444"))

answer = ("C","A","B,","D","D")
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

print("------  RESULTS  -----")
print(answer)