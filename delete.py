# import csv

# def delete_data_student(student_data):
#     student_id = student_data[0]
#     list_data_student = []
#     with open('student_base.csv', 'r', encoding='cp1251') as sb:
#         file_reader = csv.DictReader(sb, delimiter=";")
#         count = 0
#         for row in sb:
#             if count > 0:
#                 try:
#                     row = row.replace('\n', '')
#                     data_student = row.split(';')
#                     if data_student[0] not in '':
#                         list_data_student.append(data_student)
#                 except ValueError:
#                     continue
#             count += 1
#     for i in list_data_student:
#         if int(student_id) == int(i[0]):
#             index = list_data_student.index(i)
#             list_data_student.pop(index)
#     with open('student_base.csv', 'w', encoding='cp1251') as sb:
#         file_writer = csv.writer(sb, delimiter=";")
#         file_writer.writerow(['student_id', 'surname', 'name', 'date_of_birth'])
#         for i in list_data_student:
#             file_writer.writerow([i[0], i[1], i[2], i[3]])
#     # return list_data_student

import postgre as p
import interface_easygui as inf

def delete_data_student(connection):
    id = inf.menu_delete_student()
    delete_student = f"DELETE FROM students WHERE id = {id}"
    p.execute_query(connection, delete_student)

def delete_data_class(connection):
    id = inf.menu_delete_class()
    delete_class = f"DELETE FROM classes WHERE id = {id}"
    p.execute_query(connection, delete_class)
