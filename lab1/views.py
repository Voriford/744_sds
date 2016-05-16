# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from random import randint


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': main_stats,
                'excellent_students': ', '.join(Statistics.get_excellent_students(Student)),
                'bad_students': ', '.join(Statistics.get_bad_students(Student))
            }
        )
        return context


class Student:
    id = 1
    students = {}
    names = []
    ids = []

    def __init__(self, name):
        self.id = Student.id
        self.name = name
        Student.ids.append(self.id)
        Student.names.append(self.name)
        Student.id += 1

    def get_students(self):
        self.students = dict(zip(self.ids, self.names))


class Statistics:
    students_stats = []
    bad_students = []
    excellent_students = []

    def __init__(self, studentid):
        self.student_stats = {studentid: {Student.students.get(studentid): Score.scores[studentid - 1]}}
        self.students_stats.append(self.student_stats)

    def get_bad_students(self):
        return [(self.students.get(x+1)) for x in range(0, 10) if Score.average_scores[x] < 2.5]

    def get_excellent_students(self):
        return [(self.students.get(x+1)) for x in range(0, 10) if Score.average_scores[x] >= 4.5]


class Subject:
    id = 1
    names = []
    ids = []
    subjects = {}
    rsubjects = {}

    def __init__(self, name):
        self.id = Subject.id
        self.name = name
        Subject.ids.append(self.id)
        Subject.names.append(self.name)
        Subject.id += 1

    def get_subjects(self):
        self.subjects = dict(zip(self.ids, self.names))

    def get_rsubjects(self):
        self.rsubjects = dict(zip(self.names, self.ids))


class Score:
    scores = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    average_scores = [0]*10

    def __init__(self, studentid, subjectid, mark):
        self.score = mark
        self.scores[studentid - 1][subjectid - 1] = self.score

    def get_average_scores(self):
        self.average_scores = [float(sum(self.scores[i])) / (len(self.scores[i])) for i in range(0, 10)]

# students:
student1 = Student("Бомбов Антон Ярославович")
student2 = Student("Ковальчук Анастасия Олеговна")
student3 = Student("Ковчунов Петр Александрович")
student4 = Student("Крупина Алиса Александровна")
student5 = Student("Кучаев Николай Алексеевич")
student6 = Student("Лекаторчук Сергей Валерьевич")
student7 = Student("Лысак Ирина Юрьевна")
student8 = Student("Мусиенко Юрий Владимирович")
student9 = Student("Ноговицын Станислав Николаевич")
student10 = Student("Осин Иван Владимирович")

# statistics:
stats = []
for i in range(1, 11):
    stats[i] = Statistics(i)

# subjects:
subject1 = Subject('timp')
subject2 = Subject('eis')
subject3 = Subject('philosophy')
subject4 = Subject('english')
subject5 = Subject('sport')

# scores:
scores = [[0]*5]*10
for i in range(1, 11):
    for j in range(1, 6):
        scores[i][j] = Score(i, j, randint(1, 5))

# init:
Student.get_students(Student)
Subject.get_subjects(Subject)
Subject.get_rsubjects(Subject)
Score.get_average_scores(Score)
main_stats = []
for i in range(10):
    main_stats[i] = {
        'id': i + 1,
        'fio': Student.students.get(i + 1),
        'timp': Score.scores[i][Subject.rsubjects.get('timp') - 1],
        'eis': Score.scores[i][Subject.rsubjects.get('eis') - 1],
        'philosophy': Score.scores[i][Subject.rsubjects.get('philosophy') - 1],
        'english': Score.scores[i][Subject.rsubjects.get('english') - 1],
        'sport': Score.scores[i][Subject.rsubjects.get('sport') - 1],
        'average': Score.average_scores[i]
    }
