# import csv

# def change_data_student(new_student_data):
#     student_id, new_surname, new_name, new_date_of_birth = new_student_data
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
#         if i[0] == student_id:
#             i[1] = new_surname
#             i[2] = new_name
#             i[3] = new_date_of_birth
#     with open('student_base.csv', 'w', encoding='cp1251') as sb:
#         file_writer = csv.writer(sb, delimiter=";")
#         file_writer.writerow(['student_id', 'surname', 'name', 'date_of_birth'])
#         for i in list_data_student:
#             file_writer.writerow([i[0], i[1], i[2], i[3]])
#     # return list_data_student

# # print(change_data_student())

import postgre as p
import interface_easygui as inf
import output as op
import datetime

def change_data_student(new_student_data):
    student_id, *student_records = new_student_data
    student_records = tuple(student_records)
    update_students_data = (f"UPDATE students SET (surname, name, date_of_birth, class_id) = {student_records} WHERE id = {student_id}")
    p.execute_query(p.connection, update_students_data)

def change_data_class(new_class_data):
    class_id, *class_records = new_class_data
    class_records = tuple(class_records)
    update_classes_data = (f"UPDATE classes SET (number, letter) = {class_records} WHERE id = {class_id}")
    p.execute_query(p.connection, update_classes_data)
