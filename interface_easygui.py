# def Intface(i:str):
#     match i:
#         case "Welcome":
#             print('---------------------------------------------')
#             print('Вы вошли в базу данных')
#         case "Menu":
#             print('---------------------------------------------')
#             print('МЕНЮ базы данных')
#             # print('1. Импортиовать данные в справочник')
#             # print('2. Экспортировать данные из справочника')
#             print('3. добавление данных в базу данных')
#             print('4. Выход из базы данных')
#         case "End":
#             print('----------------------------------------------')
#             print('Выберите дальнейшее действие')
#             print('1. Выход в главное меню')
#             print('2. Выход из программы')

import easygui
from easygui import *  # импортируем всё
import input as ip
import output as op

def menu():
    title = 'Главное меню'
    text = 'Вы в главном меню'
    button_list = []
    button1 = 'Выход'
    button2 = 'Ученики'
    button3 = 'Классы'
    button_list.append(button1)
    button_list.append(button2)
    button_list.append(button3)
    output = buttonbox(text, title, button_list)
    return output

def menu_students():
    title = 'Ученики'
    text = 'Данные об учениках'
    button_list = []
    button0 = 'Выход'
    button1 = 'Выход в главное меню'
    button2 = 'Добавить ученика'
    button3 = 'Удалить ученика'
    button4 = 'Изменить данные об ученике'
    button5 = 'Просмотреть все данные об учениках'
    button6 = 'Экспорт в CSV'
    button7 = 'Поиск ученика'
    button_list.append(button0)
    button_list.append(button1)
    button_list.append(button2)
    button_list.append(button3)
    button_list.append(button4)
    button_list.append(button5)
    button_list.append(button6)
    button_list.append(button7)
    output_students = buttonbox(text, title, button_list)
    return output_students

def menu_class():
    title = 'Классы'
    text = 'Данные о классах'
    button_list = []
    button0 = 'Выход'
    button1 = 'Выход в главное меню'
    button2 = 'Добавить класс'
    button3 = 'Удалить класс'
    button4 = 'Изменить данные о классе'
    button5 = 'Просмотреть данные обо всех классах'
    button6 = 'Экспорт в CSV'
    button7 = 'Импорт из CSV'
    button_list.append(button0)
    button_list.append(button1)
    button_list.append(button2)
    button_list.append(button3)
    button_list.append(button4)
    button_list.append(button5)
    button_list.append(button6)
    button_list.append(button7)
    output_students = buttonbox(text, title, button_list)
    return output_students

def menu_input_student():
    title = 'Ввод данных об ученике'
    msg = 'Введите данные об ученике'
    field_text = ['Фамилия ученика', 'Имя ученика', 'Дата рождения']
    global student_data
    student_data = []
    student_data = multenterbox(msg, title, field_text)
    classes = op.read_query_classes()
    dict_of_classes = {}
    for one_class in classes:
        class_id, number, letter = one_class
        dict_of_classes[class_id] = str(number) + letter
    reply = choicebox('Выберете класс', title, choices = dict_of_classes.items())
    reply = int(reply[1:3].replace(',', ''))
    student_data.append(reply)
    return student_data

def menu_change_student():
    title = 'Изменение данных об ученике'
    msg = 'Выберете ученика'
    students = op.read_query_students()
    list_of_students = {}
    for student in students:
        student_id, surname, name, date_of_birth, class_id = student
        list_of_students[student_id] = surname + ', ' + name + ', ' + str(date_of_birth) + ', ' + str(class_id)
    reply = choicebox(msg, title, choices = list_of_students.items())
    student_id = int(reply[1:3].replace(',', ''))
    msg = 'Введите новые данные об ученике'
    field_text = [f'Фамилия ученика: {surname}; Введите новые данные: ', f'Имя ученика: {name}; Введите новые данные: ', \
    f'Дата рождения: {date_of_birth}; Введите новые данные: ']
    global student_data
    student_data = []
    student_data = multenterbox(msg, title, field_text)
    classes = op.read_query_classes()
    dict_of_classes = {}
    for one_class in classes:
        class_id, number, letter = one_class
        dict_of_classes[class_id] = str(number) + letter
    reply = choicebox('Выберете класс', title, choices = dict_of_classes.items())
    reply = int(reply[1:3].replace(',', ''))
    student_data.append(reply)
    student_data.insert(0, student_id)
    return student_data

def menu_find_student():
    title = 'Поиск ученика'
    msg = 'Введите фамилию ученика'
    surname = enterbox(msg, title)
    return surname

def menu_delete_student():
    title = 'Удаление данных об ученике'
    msg = 'Выберете ученика'
    students = op.read_query_students()
    list_of_students = {}
    for student in students:
        student_id, surname, name, date_of_birth, class_id = student
        list_of_students[student_id] = surname + ', ' + name + ', ' + str(date_of_birth) + ', ' + str(class_id)
    reply = choicebox(msg, title, choices = list_of_students.items())
    student_id = int(reply[1:3].replace(',', ''))
    return student_id

def menu_input_class():
    title = 'Ввод данных о классе'
    msg = 'Введите данные о классе'
    field_text = ['Класс', 'Буква']
    global class_data
    class_data = []
    class_data = multenterbox(msg, title, field_text)
    return class_data

def menu_delete_class():
    title = 'Удаление данных о классе'
    msg = 'Выберете класс'
    classes = op.read_query_classes()
    dict_of_classes = {}
    for one_class in classes:
        class_id, number, letter = one_class
        dict_of_classes[class_id] = str(number) + letter
    reply = choicebox('Выберете класс', title, choices = dict_of_classes.items())
    class_id = int(reply[1:3].replace(',', ''))
    return class_id

def menu_change_class():
    title = 'Изменение данных о классе'
    msg = 'Выберете класс'
    classes = op.read_query_classes()
    dict_of_classes = {}
    for one_class in classes:
        class_id, number, letter = one_class
        dict_of_classes[class_id] = str(number) + letter
    reply = choicebox('Выберете класс', title, choices = dict_of_classes.items())
    class_id = int(reply[1:3].replace(',', ''))
    msg = 'Введите новые данные о классе'
    field_text = [f'Класс: {number}; Введите новые данные: ', f'Буква: {letter}; Введите новые данные: ']
    global class_data
    class_data = []
    class_data = multenterbox(msg, title, field_text)
    class_data.insert(0, class_id)
    return class_data

