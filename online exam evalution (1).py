def validate_answers(student_answers, correct_answers):
    score = 0
    for i in range(len(correct_answers)):
        if student_answers[i] == correct_answers[i]:
            score += 1
    return score

def calculate_score(score, total_questions):
    percentage = (score / total_questions) * 100
    return percentage

def generate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"

# Main Program
correct_answers = ['A', 'B', 'C', 'D', 'A']
student_answers = []

print("Enter your answers (A/B/C/D):")
for i in range(len(correct_answers)):
    ans = input(f"Question {i+1}: ").upper()
    student_answers.append(ans)

score = validate_answers(student_answers, correct_answers)
percentage = calculate_score(score, len(correct_answers))
grade = generate_grade(percentage)

print("\n--- Exam Result ---")
print("Total Questions:", len(correct_answers))
print("Correct Answers:", score)
print("Percentage:", percentage)
print("Grade:", grade)
