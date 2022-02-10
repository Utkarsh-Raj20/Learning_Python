class Students:
    def __init__(self, name: str, age: int, marks: int) -> None:
        self.name = name
        self.age = age
        self.marks = marks


class Course:
    def __init__(self, name, max_students) -> None:
        self.name = name
        self.max_students = max_students
        self.list = []

    def add_students(self, Students):
        if len(self.list) < self.max_students:
            self.list.append(Students)
        else:
            print(f"Cannot add {Students.name}, Seats are full")

    def average_marks_of_students(self):
        sum = 0
        for people in self.list:
            sum += people.marks
        return sum / len(self.list)


utkarsh = Students("Utkarsh", 17, 87)
raju = Students("Raju", 17, 70)
kamlesh = Students("Kamlesh", 17, 50)

Science = Course("Science", 2)
Science.add_students(utkarsh)
Science.add_students(raju)

print(Science.average_marks_of_students())
