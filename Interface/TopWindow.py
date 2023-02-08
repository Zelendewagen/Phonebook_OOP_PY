import tkinter as tk

import Model
from Interface import Config
import Controller

add_window: tk.Tk
change_window: tk.Tk
add_entry = []
change_entry = []


def create_add_window():
    global add_window
    global add_entry

    RESIZABLE = False

    add_window = tk.Toplevel()
    add_window.title('Добавить контакт')
    add_window.geometry(Config.window_geometry(add_window, Config.AWW, Config.AWH))
    add_window.resizable(RESIZABLE, RESIZABLE)
    add_window.attributes("-topmost", 1)

    add_window.columnconfigure(index=0, weight=50)
    add_window.columnconfigure(index=1, weight=250)

    name_lable = tk.Label(add_window, text='Имя')
    phone_lable = tk.Label(add_window, text='Телефон')
    comment_lable = tk.Label(add_window, text='Комментарий\n(Не обязательно)')
    name_lable.grid(column=0, row=0, pady=3, sticky='e')
    phone_lable.grid(column=0, row=1, sticky='e')
    comment_lable.grid(column=0, row=2, sticky='e')

    add_entry = [tk.Entry(add_window, width=30) for _ in range(3)]
    for i, entry in enumerate(add_entry):
        add_entry[i].grid(column=1, row=i)

    add_button = tk.Button(add_window, text='Добавить',
                           command=lambda: add_contact(add_entry))
    add_button.grid(columnspan=2, pady=2, row=3)


def add_contact(add_entry: list):
    global add_window
    if add_entry[0].get() != '' and add_entry[1].get() != '' and add_entry[1].get() != '':
        Model.my_phonebook.add(
            add_entry[0].get(), add_entry[1].get(), add_entry[2].get())
    else:
        Model.my_phonebook.add('Егор', '+7-777-777-77-77', 'Домашний')
        Model.my_phonebook.add('Саня', '+7 777 777 77 77', 'Рабочий')
        Model.my_phonebook.add('Мария', '+77777777777', 'Личный')
    Controller.refresh_table()
    add_window.destroy()


def create_change_window(contact: list):
    global change_window
    global change_entry

    RESIZABLE = False

    change_window = tk.Toplevel()
    change_window.title('Изменить контакт')
    change_window.geometry(Config.window_geometry(change_window, Config.AWW, Config.AWH))
    change_window.resizable(RESIZABLE, RESIZABLE)
    change_window.attributes("-topmost", 1)

    change_window.columnconfigure(index=0, weight=50)
    change_window.columnconfigure(index=1, weight=250)

    name_lable = tk.Label(change_window, text='Имя')
    phone_lable = tk.Label(change_window, text='Телефон')
    comment_lable = tk.Label(change_window, text='Комментарий')
    name_lable.grid(column=0, row=0, pady=3, sticky='e')
    phone_lable.grid(column=0, row=1, sticky='e')
    comment_lable.grid(column=0, row=2, sticky='e')

    change_entry = [tk.Entry(change_window, width=30) for _ in range(3)]
    for i, entry in enumerate(change_entry):
        change_entry[i].insert(0, contact[i + 1])
        change_entry[i].grid(column=1, row=i)

    change_button = tk.Button(change_window, text='Изменить',
                              command=lambda: change_contact(change_entry, contact))
    change_button.grid(columnspan=2, pady=2, row=3)

    change_window.mainloop()


def change_contact(change_entry: list, contact: list):
    global change_window

    Model.my_phonebook.set(contact[0], change_entry[0].get(
    ), change_entry[1].get(), change_entry[2].get())
    Controller.refresh_table()
    change_window.destroy()


def create_save_window():
    global save_window
    #
    RESIZABLE = False

    save_window = tk.Toplevel()
    save_window.title('Формат')
    save_window.geometry(Config.window_geometry(
        save_window, Config.SWWW, Config.SWWH))
    save_window.resizable(RESIZABLE, RESIZABLE)
    save_window.attributes("-topmost", 1)

    save_window.columnconfigure(index=0, weight=50)
    save_window.columnconfigure(index=1, weight=250)

    lable = tk.Label(save_window, text='Выберите формат сохранения')
    lable.grid(row=0, column=0)

    add_button = tk.Button(
        save_window, text='ID, ФИО, Телефон, Комментарий', width=30, command=lambda: Controller.save_file('type1'))
    add_button.grid(row=1, column=0, padx=25, pady=2)
    add_button = tk.Button(
        save_window, text='ФИО, Телефон, Комментарий', width=40, command=lambda: Controller.save_file('type2'))
    add_button.grid(row=2, column=0, padx=25, pady=2)
    add_button = tk.Button(save_window, text='ФИО, Телефон', width=40, command=lambda: Controller.save_file('type3'))
    add_button.grid(row=3, column=0, padx=25, pady=2)


def create_open_window():
    #
    RESIZABLE = False

    open_file_window = tk.Toplevel()
    open_file_window.title('Формат')
    open_file_window.geometry(Config.window_geometry(
        open_file_window, Config.SWWW, Config.SWWH))
    open_file_window.resizable(RESIZABLE, RESIZABLE)
    open_file_window.attributes("-topmost", 1)

    open_file_window.columnconfigure(index=0, weight=50)
    open_file_window.columnconfigure(index=1, weight=250)

    lable = tk.Label(open_file_window, text='Выберите какой формат открыть')
    lable.grid(row=0, column=0)

    add_button = tk.Button(
        open_file_window, text='ID, ФИО, Телефон, Комментарий', width=30, command=lambda: Controller.open_file('type1'))
    add_button.grid(row=1, column=0, padx=25, pady=2)
    add_button = tk.Button(
        open_file_window, text='ФИО, Телефон, Комментарий', width=40, command=lambda: Controller.open_file('type2'))
    add_button.grid(row=2, column=0, padx=25, pady=2)
    add_button = tk.Button(open_file_window, text='ФИО, Телефон', width=40,
                           command=lambda: Controller.open_file('type3'))
    add_button.grid(row=3, column=0, padx=25, pady=2)
