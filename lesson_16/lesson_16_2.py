class Student:
    name = ''
    sex = ''
    age = 0
    grades = []


class Group:
    s1 = Student()
    s1.name = "Игорь"
    s1.sex = 'male'
    s1.age = 25
    s1.grades = [2, 3, 5, 2, 4]

    s2 = Student()
    s2.name = "Лиза"
    s2.sex = 'female'
    s2.age = 25
    s2.grades = [4, 4, 1, 5, 5]

    s3 = Student()
    s3.name = "Вася"
    s3.sex = 'male'
    s3.age = 30
    s3.grades = [4, 5, 4, 4, 4]
    students = [s1, s2, s3]
    num_of_students = len(students)

    def __init__(self, group_name):
        self.group_name = group_name

    def show_names_and_marks(self, group):
        print(f"Группа{self.group_name} (Численность:{self.num_of_students}):")
        for i in range(len(group)):
            if group[i].sex == 'male':
                print(f"Оценки студента {group[i].name} {group[i].age}"
                      f":{group[i].grades}")
            else:
                print(f"Оценки студентки {group[i].name} {group[i].age}"
                      f":{group[i].grades}")


if __name__ == '__main__':
    g = Group("A")
    g.show_names_and_marks(g.students)
