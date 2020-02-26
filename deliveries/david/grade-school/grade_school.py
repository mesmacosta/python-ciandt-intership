
class School:
    def __init__(self):
        self.list_students = list()
        self.list_data = list()

    def add_student(self, name, grade):
        self.list_students.append({"name": name, "grade": grade})

    def roster(self):
        return self.sort_student_list_by_name_and_grade()

    def grade(self, grade_number):
        return self.expect_grade_number_and_return_list_ordered(grade_number)

    def sort_student_list_by_name_and_grade(self):
        sorted_list = sorted(self.list_students, key=lambda k: (k['grade'], k['name']))
        return self.add_to_a_new_list_student_list(sorted_list)

    def add_to_a_new_list_student_list(self, list_name):
        for names_students in list_name:
            self.list_data.append(names_students["name"])
        return self.list_data

    def expect_grade_number_and_return_list_ordered(self, grade_number):
        for names_students in self.list_students:
            if names_students["grade"] == grade_number:
               self.list_data.append(names_students["name"])
        return sorted(self.list_data)



