score = 0
questions = [("What is 2 + 2?", "4"),
    ("What programming language are we learning?", "python"),
    ("What keyword is used to create a condition?", "if"), ("What is the result of (2 * 3)?", "6"),
    ("What is the capital of France?", "Paris")]
for number, (question, correct_answer) in enumerate(questions, start=1):
    print("Question:", number)
    answer = input(question + " ").strip().lower()
    if answer == correct_answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!", "\nThe correct answer is:", correct_answer)
print("\n Quiz Completed!")
print("Score:", score,"/",len(questions))
percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")
print("Excellent")
