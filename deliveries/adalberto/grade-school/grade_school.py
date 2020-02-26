import collections


class School:

    def __init__(self, db=None):
        if db is None:
            db = dict()
        self.db = db

    def add_student(self, name, grade):
        students_list = []
        if grade in self.db:
            students_list = self.db[int(grade)]
            students_list.append(name)
        else:
            students_list.append(name)
        self.db[int(grade)] = students_list

    def roster(self):
        students_list = []
        sorted_key_db = collections.OrderedDict(sorted(self.db.items(), key=lambda t: t[0]))
        for i in sorted_key_db.keys():
            sorted_key_db[i].sort()
            for j in sorted_key_db[i]:
                students_list.append(j)
        return students_list

    def grade(self, grade_number):
        if grade_number in self.db:
            sorted_key_db = collections.OrderedDict(sorted(self.db.items(), key=lambda t: t[0]))
            sorted_key_db[grade_number].sort()
            students_list = sorted_key_db[grade_number]
            return students_list
        else:
            return []
