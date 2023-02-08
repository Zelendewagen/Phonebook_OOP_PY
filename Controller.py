from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox as mb

import Model
from Interface import MainWindow
from Interface import TopWindow


def refresh_table():
    MainWindow.main_table.delete(*MainWindow.main_table.get_children())
    for row in Model.my_phonebook.show_all():
        MainWindow.main_table.insert('', 'end', values=row)


def show_search_result(search_list):
    MainWindow.main_table.delete(*MainWindow.main_table.get_children())
    for row in search_list:
        MainWindow.main_table.insert('', 'end', values=row)


def add_contact():
    TopWindow.create_add_window()


def change_contact(ID: int):
    contact = MainWindow.main_table.item(ID).get('values')
    TopWindow.create_change_window(contact)


def delete_contact(ID: int):
    contact = MainWindow.main_table.item(ID).get('values')
    if mb.askyesno('Удалить', 'Точно?'):
        Model.my_phonebook.remove(contact[0])
        refresh_table()


def new_file():
    if mb.askyesno('Создать новый справочник', 'Точно?'):
        Model.my_phonebook.clear()
        refresh_table()


def open_file(file_format):
    if file_format == 'type1':
        types = (("type1 files", "*.type1"),)
    if file_format == 'type2':
        types = ((f"{file_format}", f"*.{file_format}"),)
    if file_format == 'type3':
        types = (("type3 files", "*.type3"),)
    full_file_name = askopenfilename(title='Открыть', filetypes=types)
    Model.my_phonebook.clear()
    #
    with open(full_file_name, 'r', encoding='UTF-8') as file:
        for index, line in enumerate(file.readlines()):
            if file_format == 'type1':
                contact = line.replace('\n', '').replace("'", "").replace('"', '').split(',')
            if file_format == 'type2':
                contact = line[:-2].replace('\n', '').replace("'", "").replace('"', '').split(',')
                contact.insert(0, index)
            if file_format == 'type3':
                contact = line[:-2].replace('\n', f'{index}').replace("'", "").replace('"', '').split(',')
                contact.insert(0, index)
                contact.append('нет комментария')
            Model.my_phonebook.add(
                contact[1], contact[2], contact[3], contact[0])
        refresh_table()

    #


def save_file(file_format):
    full_file_name = asksaveasfilename(
        title='Сохранить как...', filetypes=(("Текстовый файл", f"*.{file_format}"),),
        initialfile=f'phonebook.{file_format}')
    #
    with open(full_file_name, 'w', encoding='UTF-8') as file:
        data = ''
        if file_format == 'type1':
            for contact in Model.my_phonebook.show_all():
                for item in contact:
                    data += f"'{str(item)}', "
                data += '\n'
        if file_format == 'type2':
            for contact in Model.my_phonebook.show_all():
                for item in contact[1:]:
                    data += f"'{str(item)}',"
                data += '\n'
        if file_format == 'type3':
            for contact in Model.my_phonebook.show_all():
                for item in contact[1:-1]:
                    data += f"'{str(item)}',"
                data += '\n'
        file.write(data)

    #
