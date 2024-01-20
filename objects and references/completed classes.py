from datetime import date

class CompletedCourses:
    def __init__(self, course_name: str, credits: int, completion_date: date):
        self.course_name = course_name
        self.credits = credits  # corrected to an integer
        self.completion_date = completion_date

if __name__ == '__main__':
    completed = []
    maths1 = CompletedCourses('Mathematics 1', 5, date(2020, 3, 11))
    prog1 = CompletedCourses('Programming 1', 6, date(2020, 12, 17))
    completed.append(maths1)
    completed.append(prog1)
    completed.append(CompletedCourses('Physics 2', 5, date(2020, 3, 11)))
    completed.append(CompletedCourses('Programming 2', 5, date(2020, 5, 19)))
    credits = 0
    for course in completed:
        print(course.course_name)
        credits += course.credits
    print(f'Total Credits: {credits}')
