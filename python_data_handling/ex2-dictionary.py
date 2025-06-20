# create a dictionary named student_scores where keys are student names and 
# values are their scores
student_scores = {
    "alice": 85,
    "Bob": 92,
    "chalie": 78,
    "David": 95,
    "Eve": 88,
    "Frank": 70,
}
print("---Initial student socres-----")
# Integrate through the dictionary and the print each student's name 
for name, score in student_scores.items():
    print(f"{name} : {score}")
print("\n")

# Add a new student and their score to the dictionary
new_student_name = "Grace"
New_student_score = 45
student_scores[new_student_name] = New_student_score
print(f"-----added student : {new_student_name} with score {New_student_score}")
for name, score in student_scores.items():
    print(f"{name} : {score}")
print("\n")