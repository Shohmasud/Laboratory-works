# Лабороторная работа 2

# 4. Составьте описание класса Спортсмен. Определите элементы-данные класса,
# позволяющие хранить сведения о фамилии, имени, отчестве, дате рождения, виде спорта, разряде,
# количестве медалей. Напишите программу, в которой создайте массив объектов этого класса, заполните
# его данными из текстового файла и найдите  в этом массиве всех спортсменов, занимающихся определенным видом спорта.

import xml.etree.ElementTree as ET  # импортирование модуля

tree = ET.parse('laba1_xml.xml')  # парсим
root = tree.getroot()  # родительский корень
print(root.tag)

print('Ввод')
input_word = input('Введите название видов спорта:')  # ввод пользователя


class Sportsmen:  # задание  класса

    # тело класса

    def __init__(self, first_name, last_name, patronymic, date_of_birth,
                 sport, sport_category, number_of_medals):  # инициализация аргументов класса
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.date_of_birth = date_of_birth
        self.sport = sport
        self.sport_category = sport_category
        self.number_of_medals = number_of_medals

    # объявление метода
    def workout_sportsmen(self):
        print(f'{self.last_name} этот cпортсмен тренируется каждый день')


i = 0
s = 0
class_object = ['sportsmen_1', 'sportsmen_2', 'sportsmen_3', 'sportsmen_4', 'sportsmen_5']  # объекты класса
for i in range(len(class_object)):
    class_object[i] = Sportsmen(root[i][0], root[i][1], root[i][2], root[i][3], root[i][4], root[i][5], root[i][6])
    if input_word.lower() == class_object[i].sport.text:
        print('Вывод')
        print(
            f'{class_object[i].first_name.text} {class_object[i].last_name.text}-вид спорта:{class_object[i].sport.text},{class_object[i].sport_category.text}, '
            f'{class_object[i].number_of_medals.text}')
        break
    i += 1
if s == 0:
    print('Такого вида спорта не существует')
