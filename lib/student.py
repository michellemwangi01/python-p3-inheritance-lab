#!/usr/bin/env python

from user import User


class Student(User):
    def __init__(self, first_name, last_name, knowledge=None):
        super().__init__(first_name, last_name)
        if knowledge is None:
            self.knowledge = []
        else:
            self.knowledge = knowledge

    def learn(self, lesson):
        self.knowledge.append(lesson)


nwestu = Student("fname", "lname", [])
nwestu.first_name