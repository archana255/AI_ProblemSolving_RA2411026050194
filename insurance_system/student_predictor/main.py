# Simple Regression-like predictor

print("Enter Student Details:\n")

study_hours = float(input("Study Hours per day: "))
attendance = float(input("Attendance (%): "))

# Simple formula (you can say it's regression)
predicted_score = (study_hours * 10) + (attendance * 0.5)

print("\nPredicted Score:", round(predicted_score, 2))

if predicted_score >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
