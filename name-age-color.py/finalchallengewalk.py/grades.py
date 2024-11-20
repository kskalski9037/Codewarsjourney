# Final Challenge: Build a program that asks the user to input their exam score and then prints a message.

# Outputs should be as follows:
# "Excellent" if the score is greater than 90.
# "Good" if the score is between 70 and 90.
# "Needs Improvement" if the score is below 70.

exam_score = input("Input your exam score")

if (exam_score > 90):
    print("Excellent")
elif (exam_score < 90 and > 70):
    print("Good")
else
    print("Needs Improvement")