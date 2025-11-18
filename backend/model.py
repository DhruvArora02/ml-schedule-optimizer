class StressModel:
    def predict(self, task):
        duration = task["duration"]
        deadline_hrs = task["deadline_hrs"]
        difficulty = task["difficulty"]

        # simple interpretable stress formula
        stress = (difficulty * 0.5) + (duration * 0.3) + (1 / (deadline_hrs + 1)) * 10
        return round(stress, 2)

model = StressModel()
