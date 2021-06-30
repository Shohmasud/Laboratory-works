# Лабораторная работа 5
# 3. Выполните следующее задание:
# разработайте приложение «Браузер файлов» поддерживающее следующие действия:
# •	вывод информации о логических дисках компьютера;
# •	 вывод дерева файлов и папок;
# •	предоставление информации о выделенных файле или папки ¬ дате создания, размере, атрибутах, времени последней модификации;
# •	 выполнение операций создания, копирования, переименования, перемещения файлов и папок.
# Интерфейс программы должен поддерживаться с помощью главного меню, контекстного меню и панелей инструментов.
# В главном меню предусмотрите пункт О программе, при выборе которого будет выводиться диалоговое окно, содержащее справочную информацию.



from tkinter import *
import os
import os.path
import re
import datetime
import shutil

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry("700x760+600+150")
box = []


def function_adr():
    global get_file
    get_file = text_box_file.get()


def f1():
    global get_name_path
    get_name_path = text_box_path.get()
    func_result_1()


def func_res_bl3():
    get_size = os.stat(f'{get_name_path}/{get_file}')
    get_s = get_size.st_size
    get_last_cr = int(get_size.st_mtime)
    get_last_dost = int(get_size.st_atime)
    get_t1 = int(get_size.st_ctime)
    dt_cr = datetime.datetime.fromtimestamp(get_t1).strftime("%d.%m.%Y %H:%M")
    dt_last_dost = datetime.datetime.fromtimestamp(get_last_dost).strftime("%d.%m.%Y %H:%M")

    dt_cr_last = datetime.datetime.fromtimestamp(get_last_cr).strftime("%d.%m.%Y %H:%M")
    label_name_p = Label(window, text=get_file,
                         font='Arial 9 bold')
    label_name_p.place(x=102, y=421)
    label_name_siz = Label(window, text=get_s,
                           font='Arial 9 bold ')
    label_name_siz.place(x=51, y=481)
    label_name_tim = Label(window, text=dt_cr,
                           font='Arial 9 bold')
    label_name_tim.place(x=402, y=481)

    label_last_cr = Label(window, text=dt_cr_last,
                          font='Arial 9 bold')
    label_last_cr.place(x=51, y=551)

    label_last_dost = Label(window, text=dt_last_dost,
                            font='Arial 9 bold')
    label_last_dost.place(x=401, y=551)


def func_result_1():
    list_path = os.listdir(get_name_path)

    if len(list_path) > 0:
        scrollbar = Scrollbar(window, width=40)
        scrollbar.place()
        my_list = Listbox(frame2, yscrollcommand=scrollbar.set, height=5, width=30)
        my_list2 = Listbox(frame1, yscrollcommand=scrollbar.set, height=5, width=30)

        for word in list_path:
            if os.path.isfile(f'{get_name_path}/{word}'):
                my_list2.insert(END, str(word))
            if os.path.isdir(f'{get_name_path}/{word}'):
                my_list.insert(END, str(word))

        my_list.pack(side=LEFT, fill=BOTH)
        my_list2.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=my_list.yview)
        if os.path.exists(f'{get_name_path}/{get_file}'):
            func_res_bl3()


def function_name_folder_file_path():
    global text_box_file
    global text_box_path
    scrollbar = Scrollbar(window)

    label_text_name_file = Label(window, text='Введите имя файла или папки и нажмите кнопку "Отобразить"',
                                 font='Arial 10 bold')
    label_text_name_file.place(x=20, y=10)
    text_box_file = Entry(window, width=80)
    text_box_file.place(x=20, y=50)
    button_ot = Button(text="Отобразить", font='Arial 9 bold', bg='white',
                       fg='black', command=f1,
                       relief=GROOVE, width=20)
    button_ot.place(x=520, y=47.5)
    # 2

    label_text_name_path = Label(window, text='Путь к папки',
                                 font='Arial 11 normal')
    label_text_name_path.place(x=20, y=80)
    text_box_path = Entry(width=60)
    text_box_path.place(x=20, y=110)
    button_v = Button(text="Вверх", command=function_adr, font='Arial 9 bold', bg='white',
                      fg='black',
                      relief=GROOVE, width=20, )
    button_v.place(x=520, y=108)


function_name_folder_file_path()


def function_text_box():
    global frame1
    global frame2
    label_text_name_file2 = Label(window, text='Файлы',
                                  font='Arial 11 normal')
    label_text_name_file2.place(x=400, y=170)
    frame1 = Frame(master=window, width=200, height=100, bg="white", borderwidth=2, relief=RIDGE)
    frame1.place(x=55, y=200)

    label_text_name_path2 = Label(window, text='Папки',
                                  font='Arial 11 normal')
    label_text_name_path2.place(x=55, y=170)
    frame2 = Frame(master=window, width=200, height=100, bg="white", borderwidth=2, relief=RIDGE)
    frame2.place(x=390, y=200)


function_text_box()


def function_information():
    label_text_name_inform = Label(window, text='Детальная нформация о выделенном файле',
                                   font='Arial 10 bold')
    label_text_name_inform.place(x=20, y=390)

    # 2
    label_text_name_inf_name = Label(window, text='Имя',
                                     font='Arial 11 normal')
    label_text_name_inf_name.place(x=20, y=420)
    text_box_name = Text(width=60, height=1)
    text_box_name.place(x=100, y=420)

    # 3
    label_text_name_inf_r = Label(window, text='Размер',
                                  font='Arial 11 normal')
    label_text_name_inf_r.place(x=50, y=450)
    text_box_r = Text(width=30, height=1)
    text_box_r.place(x=50, y=480)

    # 4
    label_text_name_inf_time = Label(window, text='Дата создания',
                                     font='Arial 11 normal')
    label_text_name_inf_time.place(x=400, y=450)
    text_box_time = Text(width=30, height=1)
    text_box_time.place(x=400, y=480)

    # 5
    label_text_name_inf_time_mod = Label(window, text='Время последней модификации',
                                         font='Arial 11 normal')
    label_text_name_inf_time_mod.place(x=50, y=520)
    text_box_time_mod = Text(width=30, height=1)
    text_box_time_mod.place(x=50, y=550)

    # 6
    label_text_name_inf_time_mod_last = Label(window, text='Время последней доступа',
                                              font='Arial 11 normal')
    label_text_name_inf_time_mod_last.place(x=400, y=520)
    text_box_time_mod_last = Text(width=30, height=1)
    text_box_time_mod_last.place(x=400, y=550)


function_information()


def function_paste():
    get_past_text = str(text_box_new.get())
    os.replace(f'{get_name_path}/{get_file}', get_past_text)


def function_copy():
    get_past_text = str(text_box_new.get())
    shutil.copy2(f'{get_name_path}/{get_file}', get_past_text)


def function_del():
    get_past_text = str(text_box_new.get())
    os.remove(get_past_text)


def function_option():
    global text_box_new
    label_text_last_div = Label(window, text='Перемещение.удаление или копирование файла',
                                font='Arial 10 bold')
    label_text_last_div.place(x=23, y=600)
    button_paste = Button(text="Перемещение", font='Arial 9 bold', bg='white',
                          fg='black', command=function_paste,
                          relief=GROOVE, width=20)
    button_paste.place(x=23, y=630)
    button_copy = Button(text="Копирование", font='Arial 9 bold', bg='white',
                         fg='black', command=function_copy,
                         relief=GROOVE, width=20)
    button_copy.place(x=230, y=650)
    button_del = Button(text="Удаление", font='Arial 9 bold', bg='white',
                        fg='black', command=function_del,
                        relief=GROOVE, width=20)
    button_del.place(x=450, y=630)

    label_text_last_div = Label(window, text='Новый',
                                font='Arial 10 normal')
    label_text_last_div.place(x=23, y=700)
    text_box_new = Entry(width=80)
    text_box_new.place(x=120, y=700)


function_option()

window.mainloop()

