

# def Reader():

#             x = input('Введите Фамилию:')
#             y = input('Введите Имя:')
#             z = input('Введите телефон:')
#             h = input('Введите номер класса:')
#             return x+y+z+h

# Reader()
            
#  # Метод считывает и возвращает считанные данные с файла file_name
# def read_text_from_file(file_name):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         data = file.read()
#     return data

# # Метод позволяет записать текст в файл
# def write_text_in_file(file_name, text):
#     with open(file_name, 'w', encoding='utf-8') as file:
#         file.write(text)
           


# import hello as h  

# print(h.f(1))

# import hello as h  

# print(h.f(1))

import csv
import output as op
import postgre as p

# def input_data_student(student_data):
#     student_id = max(op.output_data_student().keys()) + 1
#     surname, name, date_of_birth = student_data
#     with open('student_base.csv', 'a', encoding='cp1251') as sb:
#         file_writer = csv.writer(sb, delimiter=";")
#         # file_writer.writerow(['student_id', 'surname', 'name', 'date_of_birth'])
#         file_writer.writerow([str(student_id), surname, name, date_of_birth])

# def input_data_class(class_data):
#     class_id = max(op.output_data_class().keys()) + 1
#     number, letter = class_data
#     with open('class_base.csv', 'a', encoding='cp1251') as cb:
#         file_writer = csv.writer(cb, delimiter=";")
#         # file_writer.writerow(['class_id', 'number', 'letter'])
#         file_writer.writerow([str(class_id), number, letter])

def input_data_student(student_data):
    student_records = tuple(student_data)
    insert_query = (f"INSERT INTO students (surname, name, date_of_birth, class_id) VALUES {student_records}")
    p.connection.autocommit = True
    cursor = p.connection.cursor()
    cursor.execute(insert_query)

def input_data_class(class_data):
    class_records = tuple(class_data)
    insert_query = (f"INSERT INTO classes (number, letter) VALUES {class_records}")
    p.connection.autocommit = True
    cursor = p.connection.cursor()
    cursor.execute(insert_query)


