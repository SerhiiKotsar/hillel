"""
Create a class with a description of the worker. Any worker. employees.
Should be @property and @name.setter + method __str__
"""


class Worker:
    def __init__(self, name, position, salary, experience):
        self._name = name
        self._position = position
        self._salary = salary
        self._experience = experience

    def __str__(self):
        return f'{self._name} is a {self._position} with {self._salary} salary and {self._experience} years experience'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError('Name should be string data type')
        self._name = new_name

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        if not isinstance(new_position, str):
            raise ValueError('Position should be string data type')
        self._position = new_position

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < 1200:
            raise ValueError('We cannot hire for less than 1200')
        self._salary = new_salary

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, new_experience):
        if new_experience == 0:
            raise ValueError('We cannot hire without experience at all')
        self._experience = new_experience
