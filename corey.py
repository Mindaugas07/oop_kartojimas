from typing import List

# class Employee:
#     num_of_emps = 0
#     raise_amt = 1.04

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + "." + last + "@email.com"
#         self.pay = pay

#         Employee.num_of_emps += 1

#     def fullname(self):
#         return "{} {}".format(self.first, self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)

#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amt = amount

#     @classmethod
#     def from_emp_string(cls, emp_str: str) -> "Employee":
#         first, last, pay = emp_str.split("-")
#         return cls(first, last, pay)

#     @staticmethod
#     def is_workday(day) -> bool:
#         if day.weekday() == 5 or day.weekday() == 6:
#             return False
#         else:
#             return True


# import datetime

# my_date = datetime.date(2024, 1, 28)
# print(Employee.is_workday(my_date))

# # emp_str_1 = "John-Doe-70000"
# # emp_str_2 = "Steve-Smith-30000"
# # emp_str_3 = "Jane-Doe-90000"


# # emp_1 = Employee.from_emp_string(emp_str_1)
# # print(emp_1.fullname())


class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@email.com"
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)


class Developer(Employee):
    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees: List["Employee"] = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_empl(self, empl):
        if empl not in self.employees:
            self.employees.append(empl)

    def remove_empl(self, empl):
        if empl in self.employees:
            self.employees.remove(empl)

    def print_employees(self):
        for empl in self.employees:
            print("-->", empl.fullname())


dev_1 = Developer("Corey", "Schafer", 50000, "Python")
dev_2 = Developer("Test", "Employee", 60000, "Java")

mgr_1 = Manager("Kestutis", "Algirdaitis", 100000, [dev_1])

print(issubclass(Manager, Employee))

# print(mgr_1.email)
# mgr_1.add_empl(dev_2)
# mgr_1.print_employees()
# # print(dev_2.email)
# # print(dev_1.pay)
# # dev_1.apply_raise()
# # print(dev_1.pay)
