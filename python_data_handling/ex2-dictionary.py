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




# find the student with highset score and print their name and score
if student_scores: # ensure the dictionary is not empty
    highest_score = 0
    highest_scorer_name = ""
    for name, score in student_scores.items():
        if score > highest_score:
            highest_score = score
            highest_scorer_name = name
    print(f"-----student with highest score---")
    print(f"{highest_scorer_name}: {highest_score}\n")
else:
    print("The dictionary is empty. cannot find the highest score.\n")