"""

"""
from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name, title):
        self.name = name
        self.title = title

    def do_work(self):
        raise NotImplementedError

    def do_relax(self):
        raise NotImplementedError


# Engineer, skill
# do work, coding
# do relax, youtube
# do refactor
class Engineer(Employee):

    def __init__(self, name, title, skill):
        super().__init__(name, title)
        self.skill = skill

    def do_work(self):
        print(f"{self} is coding, and skill is {self.skill}")

    def do_relax(self):
        print(f"{self} is watch youtube")

    def do_refactor(self):
        print(f"{self} is refactor")


# Manager, direct_reports
# do work, meeting
# do relax, trip
# do hire employee
class Manager(Employee):

    def __init__(self, name, title, direct_reports):
        super().__init__(name, title)
        self.direct_reports = direct_reports

    def do_work(self):
        print(f"{self} is meeting with {self.direct_reports}")

    def do_relax(self):
        print(f"{self} is  trip")

    def do_hire(self):
        print(f"{self} is hire")


def main():
    print("main")
    # two engineer
    e1 = Engineer("betty", "backend", "golang")
    e2 = Engineer("cc", "backend", "nodejs, python, scala")
    assert isinstance(e1, Employee)
    assert not isinstance(e1, Manager)
    print(e2.do_work())
    print(e2.do_relax())
    print(e2.do_refactor())
    # a manager
    m1 = Manager("wan zun", "cto", "ceo")
    print(m1.do_work())
    print(m1.do_relax())
    print(m1.do_hire())
    assert isinstance(m1, Manager)
    assert not isinstance(m1, Engineer)


if __name__ == '__main__':
    main()
