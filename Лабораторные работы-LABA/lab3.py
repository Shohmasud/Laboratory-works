# Лабороторная работа 3
#
# 4. Создать абстрактный класс Персона. На его основе реализовать классы Служащий, Рабочий, инженер.
# Класс Персона должен содержать атрибуты и методы, общие для производных классов. Основная программа
# должна создавать массивы объектов производных классов и выводить их на экран.


from abc import ABC, abstractmethod


class Person(ABC):  # задание  класса

    # тело класса

    def __init__(self, first_name, last_name, work_category, watch_work):  # инициализация аргументов класса
        self.first_name = first_name
        self.last_name = last_name
        self.work_category = work_category
        self.watch_work = watch_work
        self.__private = 'private'

    @abstractmethod
    def work_person(self):
        pass

    @abstractmethod
    def aet_person(self):
        pass


class Employee(Person):
    def __init__(self, first_name, last_name, work_category, watch_work):
        super().__init__(first_name, last_name, work_category, watch_work)

    def aet_person(self):
        print('кушают')

    def work_person(self):
        print('работают')


class Work(Person):
    def __init__(self, first_name, last_name, work_category, watch_work):
        super().__init__(first_name, last_name, work_category, watch_work)

    def aet_person(self):
        print('отдыхает')

    def work_person(self):
        print('не работают')


class Engineer(Person):
    def __init__(self, first_name, last_name, work_category, watch_work):
        super().__init__(first_name, last_name, work_category, watch_work)

    def aet_person(self):
        print('много работает')

    def work_person(self):
        print('кушает')


employee = Employee('Виктор', 'Кириллов', 'служащий', '8 часов')
work = Work('Виталий', 'Орловский', 'рабочий', '12 часов')
engineer = Engineer('Андрей', 'Кириллов', 'инжинер', '9 часов')

massive = [employee, work, engineer]
if __name__ == '__main__':
    for i in massive:
        print(i.first_name, i.last_name, i.work_category, i.watch_work)
        i.aet_person()
        i.work_person()
