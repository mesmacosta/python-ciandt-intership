class School:
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        self.students.append(
            {
                'name': name,
                'grade': grade
            }
        )

    # Sort students for their grades and their names. Grades more important than names
    def __sort(self):
        self.students.sort(key=lambda d: d['name'])
        self.students.sort(key=lambda d: d['grade'])

    def roster(self):
        self.__sort()
        student_names = [student['name'] for student in self.students]
        return student_names

    def grade(self, grade_number):
        student_names = [student['name'] for student in self.students if student['grade'] == grade_number]
        student_names.sort()
        return student_names
