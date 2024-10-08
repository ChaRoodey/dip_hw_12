import csv


class Student:
    def __init__(self, name, subjects_file: str):
        self.__setattr__('name', name)
        self.subjects = {}
        self.load_subjects(subjects_file)

    def __setattr__(self, name, value):
        if name == 'name':
            if not isinstance(value, str) and not value[0].isupper():
                raise ValueError('ФИО должно состоять из букв и начинаться с заглавной')
            super().__setattr__('name', name)

    def __getattr__(self, name):
        return name

    def __str__(self):
        return f'Студент: {self.name}\nПредмет: {", ".join(i for i in self.subjects.keys())}'

    def load_subjects(self, subjects_file):
        try:
            with open(subjects_file, 'r', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file)
                for row in reader:
                    for subject in row:
                        self.subjects[subject] = {'grades': [], 'test_score': []}
        except FileNotFoundError:
            raise FileNotFoundError('Файл с таким именем не найден')

    def add_grade(self, subject, grade):
        if 2 <= grade <= 5:
            self.subjects[subject]['grades'].append(grade)
        else:
            raise ValueError('Оценка должна быть от 2 до 5')

    def add_test_score(self, subject, test_score):
        if 0 <= test_score <= 100:
            self.subjects[subject]['test_score'].append(test_score)
        else:
            raise ValueError('Оценка за тест должна быть от 0 до 100')

    def get_average_test_score(self, subject):
        all_scors = 0
        amount_test_scors = len(self.subjects[subject]["test_score"])

        for score in self.subjects[subject]["test_score"]:
            all_scors += score

        return all_scors / amount_test_scors

    def get_average_grade(self, subject):
        all_grades = 0
        amount_grade = len(self.subjects[subject]["grades"])

        for grade in self.subjects[subject]["grades"]:
            all_grades += grade

        return all_grades / amount_grade


if __name__ == '__main__':
    student = Student("Иван Иванов", "subjects.csv")
    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)
    student.add_grade("История", 5)
    student.add_test_score("История", 92)
    average_grade = student.get_average_grade('Математика')
    print(f"Средний балл: {average_grade}")
    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")
    print(student)
