class Student:
    def __init__(self, name: str, student_number: str):
        self.name = name
        self.student_number = student_number
        self.study_credits = 0
    def add_credits(self, study_credits):
        if study_credits > 0:
            self.study_credits += study_credits
if __name__ == '__main__':
    sally = Student("Sally Student", "12345")
    sally.add_credits(5)
    sally.add_credits(5)
    sally.add_credits(10)
    print("Study credits:", sally.study_credits)