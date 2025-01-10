students_scores = [
    [85, 90, 78, 92, 88],
    [75, 80, 85],
    [90, 88, 92, 94]
]

for i, scores in enumerate(students_scores):
    print(f"Student {i+1} Scores: {scores}")
    average_score = sum(scores) / len(scores)
    print(f"Average Score of Student {i+1}: {average_score:.2f}")
    print("-" * 30)
