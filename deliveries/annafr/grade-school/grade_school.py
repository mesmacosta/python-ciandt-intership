class School:
    def __init__(self):
        self.grade_school = {}

    def add_student(self, name, grade):
        grade = str(grade)
        value = self.grade_school.get(grade)
        if value:
            value.append(name)
            self.grade_school.update({grade: value})
            return
        self.grade_school.update({grade: [name]})

    def roster(self):
        class_ordered = [sorted(self.grade_school[key], key=lambda v: v.upper())
                         for key in sorted(self.grade_school.keys())]

        students = []
        for student in class_ordered:
            students = students + student
        return students

    def grade(self, grade):
        grade_number = str(grade)
        return sorted(self.grade_school.get(grade, []))


# school = School()
# school.add_student("Anna", 1)
# school.add_student("Arthur", 5)
# school.add_student("Jorge", 2)
# school.add_student("sadasdas", 2)
# school.add_student("ZJorgdsadsadase", 2)
# school.roster()
# # pdb.set_trace()  # breakpoint 3e5b211b //
#
# School().grade(1)