class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.__marks = marks

    def display_details(self):
        print(f"Name    : {self.name}")
        print(f"Roll No : {self.roll_no}")
        print(f"Marks   : {self.__marks}")

    def get_grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 75:
            return "B"
        elif self.__marks >= 60:
            return "C"
        elif self.__marks >= 40:
            return "D"
        else:
            return "F"


class GraduateStudent(Student):
    def __init__(self, name, roll_no, marks, specialization):
        super().__init__(name, roll_no, marks)
        self.specialization = specialization

    def display_details(self):
        super().display_details()
        print(f"Specialization : {self.specialization}")


# Creating objects
student1 = Student("Rahul", 101, 85)
student2 = GraduateStudent("Priya", 102, 92, "Computer Science")

print("Student 1 Details")
student1.display_details()
print("Grade:", student1.get_grade())

print("\nStudent 2 Details")
student2.display_details()
print("Grade:", student2.get_grade())