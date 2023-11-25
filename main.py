class EntranceExamination:
    def __init__(self):
        self.subjects = ["English", "Mathematics", "Physics", "Chemistry"]
        self.candidates = ["Taiwo", "Kenny", "Usman", "Nkechi", "Ofure"]
        self.scores = []

    def populate_scores(self, scores):
        self.scores = scores

    def display_scores(self):
        print("Candidate\tEnglish\tMathematics\tPhysics\tChemistry")
        for i in range(len(self.candidates)):
            print(self.candidates[i], end="\t\t")
            for j in range(len(self.subjects)):
                print(self.scores[i][j], end="\t\t")
            print()
exam = EntranceExamination()
scores = [
    [56, 43, 57, 60],
    [76, 56, 67, 68],
    [47, 38, 75, 59],
    [37, 49, 64, 58],
    [58, 75, 57, 60]
]
exam.populate_scores(scores)
exam.display_scores()

scores = {
    "Taiwo": [56, 43, 57, 60],
    "Kenny": [76, 56, 67, 68],
    "Usman": [47, 38, 75, 59],
    "Nkechi": [37, 49, 64, 58],
    "Ofure": [58, 75, 57, 60]
}

for candidate, candidate_scores in scores.items():
    average_score = sum(candidate_scores) / len(candidate_scores)
    print(f"Average score for {candidate}: {average_score:.2f}")

max_score = max([max(candidate_scores) for candidate_scores in scores.values()])

print(f"{max_score}")

max_score = max(max(candidate_scores) for candidate_scores in scores.values())

for candidate, candidate_scores in scores.items():
    if max_score in candidate_scores:
        subject_index = candidate_scores.index(max_score)
        subject = ["English", "Mathematics", "Physics", "Chemistry"][subject_index]
        print(f"The student with the maximum score is {candidate} in the subject {subject} with a score of {max_score}")



