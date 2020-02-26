class School:
    def __init__(self):
        self._db = {}

    def add_student(self, name, grade):
        self._db[grade] = self._db.get(grade, [])
        self._db[grade].append(name)
        self._db[grade].sort()

    def roster(self):
        tmp = []
        for grade in sorted(self._db.keys()):
            tmp = [*tmp, *self._db[grade]]
        return tmp


    def grade(self, grade_number):
        return self._db.get(grade_number, [])