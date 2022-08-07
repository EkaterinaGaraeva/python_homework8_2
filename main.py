# import interface as Iface
# import output as ot
# import input as It

import easygui
from easygui import *
import input as ip
import output as op
import interface_easygui as inf
import change as ch
import delete as d
import postgre as p
import export as ex
import find as f

def main_menu():
    output = inf.menu()
    while True:
        match output:
            case 'Выход':
                break
            case 'Ученики':
                output_students = inf.menu_students()
                match output_students:
                    case 'Выход':
                        break
                    case 'Выход в главное меню':
                        output = inf.menu()
                    case 'Добавить ученика':
                        student_data = inf.menu_input_student()
                        try:
                            ip.input_data_student(student_data)
                        except TypeError:
                            msgbox('Не удалось добавить данные', 'Ошибка')
                            continue
                    case 'Удалить ученика':
                        try:
                            d.delete_data_student(p.connection)
                        except TypeError:
                            msgbox('Не удалось удалить данные', 'Ошибка')
                            continue
                    case 'Изменить данные об ученике':
                        new_student_data = inf.menu_change_student()
                        try:
                            ch.change_data_student(new_student_data)
                        except TypeError:
                            msgbox('Не удалось изменить данные', 'Ошибка')
                            continue
                    case 'Просмотреть все данные об учениках':
                        students = op.read_query_students()
                        text = op.output_query_students(students)
                        msgbox(text, 'Данные об учениках')
                    case 'Экспорт в CSV':
                        ex.export_csv_data_student()
                    case 'Поиск ученика':
                        surname = inf.menu_find_student()
                        students = f.find_student(surname)
                        text = f.output_find_student(students)
                        msgbox(text, 'Найдены ученики')
            case 'Классы':
                output_class = inf.menu_class()
                match output_class:
                    case 'Выход':
                        break
                    case 'Выход в главное меню':
                        output = inf.menu()
                    case 'Добавить класс':
                        class_data = inf.menu_input_class()
                        try:
                            ip.input_data_class(class_data)
                        except TypeError:
                            msgbox('Не удалось добавить данные', 'Ошибка')
                            continue
                    case 'Удалить класс':
                        try:
                            d.delete_data_class(p.connection)
                        except TypeError:
                            msgbox('Не удалось удалить данные', 'Ошибка')
                            continue
                    case 'Изменить данные о классе':
                        new_class_data = inf.menu_change_class()
                        try:
                            ch.change_data_class(new_class_data)
                        except TypeError:
                            msgbox('Не удалось изменить данные', 'Ошибка')
                            continue
                    case 'Просмотреть данные обо всех классах':
                        classes = op.read_query_classes()
                        text = op.output_query_classes(classes)
                        msgbox(text, 'Данные обо всех классах')
                    case 'Экспорт в CSV':
                        ex.export_csv_data_class()


main_menu()

