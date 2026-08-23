student_name = input("Enter your name:")
score = float(input("Enter you score:"))
percentage = score
even_score = score % 2 == 0
passed = score >= 50

print("======================")
print("    SCORE ANALYZER    ")
print("======================")
print("Name:", student_name)
print("Score:", score)
print()
print("Score:", percentage)
print("Passed:", passed)
print("Even Score:", even_score)
print("======================")


