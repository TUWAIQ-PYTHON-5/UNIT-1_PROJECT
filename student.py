class student():
    def __init__(self, name: str, age: int, gender: str, GPA: float, DNA: float) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.GPA = GPA
        self.DNA = DNA

    def student_GPA(self):
        if self.GPA >= 4.50:
            msg1 = "Exlent"
            return msg1

        elif self.GPA < 4.50 and self.GPA >= 3.75:
            msg2 = "Very Good"
            return msg2

        elif self.GPA < 3.75 and self.GPA >= 2.75:
            msg3 = "Good"
            return msg3

        elif self.GPA < 2.75 and self.GPA >= 2.00:
            msg4 = "Acceptable"
            return msg4

        else:
            return "fail"

    def add_list(self):

        new_list = []

        new_list.append(student(self.name, self.age, self.gender, self.GPA, self.DNA))
        return new_list

    def print_student(self):
        x = self.add_list()
        for i in x:
            print(i)

    # DNA IS APERSENT OF APSENT
    def attendance_rate(self) -> float:
        persent = float(self.DNA)
        return persent

    def is_student_status_DNA(self):
        DNA = self.attendance_rate()
        if DNA >= 25.0:
            msg5 = (f"{self.name} ٍStudet ok Passed !")
            return msg5
        else:
            msg6 = (f"{self.name} fail !Exceed the limit ")
            return msg6

