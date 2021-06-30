# 4. Написать приложение, которое по заданным в файле исходным данным выводит информацию о компьютерах. Создать меню
# с командами Choose, Show, Quit.
# Команда Show недоступна.
# При запуске приложения из файла должны читаться исходные данные. Файл необходимо сформировать самостоятельно. Каждая строка файла должна содержать тип компьютера, цену (price) и емкость жесткого диска (hard drive).
# При выборе команды Choose должно открываться диалоговое окно, содержащее:
# – поле типа TextBox для ввода минимальной емкости диска;
# – поле типа TextBox для ввода максимальной приемлемой цены;
# – группу из двух переключателей Hard drive и Price типа RadioButton;
# – кнопки OK и Cancel типа Button.
# После ввода всех данных команда меню Show становится доступной. Эта команда должна открывать диалоговое окно, содержащее список компьютеров, удовлетворяющий введенным ограничениям и упорядоченный по отмеченной характеристике.
# Команда Quit должна завершать работу приложения.


from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Radiobutton

box_drive = []
box_price = []

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry("400x100+700+250")


def function_show():
    if len(box_drive) and len(box_price) < 1:
        pass


def choose_window():
    i = 0
    global window_two
    window_two = Tk()
    window_two.title("Choose")
    window_two.geometry('400x390+1101+250')
    window_two['bg'] = '#bdbbbb'
    if i == 0:
        function_choose()


button_menu = Menu(tearoff=0)
button_menu_choose = button_menu.add_command(label='Choose', command=choose_window)
button_menu_show = button_menu.add_command(label='Show', command=function_show)
button_menu_quit = button_menu.add_command(label='Quit')



def function_ok():
    if var.get() == 1:
        box_drive.append(combo.get())
        button_ok.destroy()
    if var.get() == 2:
        # box_price.append(text_box_price.get())
        button_ok.destroy()


def function_choose():
    box = []
    global var
    global label_text_box_type
    global combo
    global label_text_box_price
    global text_box_price
    global radio_button_hard_drive
    global radio_button_price
    global button_ok
    global button_cancel
    global button_show_two

    label_text_box_type = Label(window_two, text="TEXT_BOX HARD DRIVE(GB)", font='Arial 9 bold')
    label_text_box_type.place(x=50, y=60)
    combo = Combobox(window_two)
    combo['values'] = (120, 240, 500, 1000, 2000)
    combo.current(0)
    combo.place(x=53, y=90)

    label_text_box_price = Label(window_two, text="TEXT_BOX HARD PRICE(RUB)", font='Arial 9 bold')
    label_text_box_price.place(x=50, y=170)
    text_box_price = Entry(window_two, width=15)
    text_box_price.place(x=53, y=200)

    var = IntVar()
    var.set(1)
    radio_button_hard_drive = Radiobutton(window_two, text='Hard Drive', variable=var, value=1)
    radio_button_hard_drive.place(x=250, y=90)
    radio_button_price = Radiobutton(window_two, text='Price', variable=var, value=2)
    radio_button_price.place(x=250, y=200)
    box.append(var.get())
    # t = Label(window_two, text=box, font='Arial 20 bold')
    # t.place(x=280, y=200)

    button_ok = Button(window_two, text="Ok", command=function_ok, font='Arial 9 bold', bg='#de7e10', fg='white',
                       relief=GROOVE)
    button_ok.place(x=220, y=310, width=40, height=30)
    button_cancel = Button(window_two, text="Cancel", command=window_two.destroy, font='Arial 9 bold', bg='#de7e10',
                           fg='white',
                           relief=GROOVE)
    button_cancel.place(x=310, y=310, width=40, height=30)



window.config(menu=button_menu)
window.mainloop()
# print(box_drive, box_price)



























# from tkinter import *
#
# root = Tk()
# root.title("Пример работы флажков")
# root.minsize(width=500, height=400)
#
# var0 = StringVar()  # значение каждого флажка
# var1 = StringVar()  # хранится в собственной переменной
# var2 = StringVar()
#
# # если флажок установлен, то в ассоциированную переменную
# # (var0, var1 или var2) заносится значение onvalue,
# # если флажок снят, то - offvalue.
#
# ch0 = Checkbutton(root, text="Windows", variable=var0, onvalue="Выбран Windows", offvalue="-")
# ch1 = Checkbutton(root, text="Linux", variable=var1, onvalue="Выбран Linux", offvalue="-")
# ch2 = Checkbutton(root, text="MacOS", variable=var2, onvalue="Выбран MacOS", offvalue="-")
#
# lis = Listbox(root, height=3)


# def result(event):
#     v0 = var0.get()
#     v1 = var1.get()
#     v2 = var2.get()
#     l = [v0, v1, v2]  # значение переменных заносится в список
#     lis.delete(0, 2)  # предыдущее значение удаляется из Listbox
#
#     for v in l:  # содержимое списка l последовательно
#         lis.insert(END, v)  # вставляется в Listbox
#
#
# but = Button(root, text="Получить значения")
# but.bind('<Button-1>', result)
#
# ch0.deselect()  # по умолчанию флажки сняты
# ch1.deselect()
# ch2.deselect()
#
# ch0.pack()
# ch1.pack()
# ch2.pack()
# but.pack()
# lis.pack()
#
# # запускаем программу
# root.mainloop()

















#
#
# from tkinter import *
#
#
# def change():
#     if var.get() == 0:
#         label['bg'] = 'red'
#     elif var.get() == 1:
#         label['bg'] = 'green'
#     elif var.get() == 2:
#         label['bg'] = 'blue'
#
#
# root = Tk()
#
var = IntVar()
var.set(1)
red = Radiobutton(text="Red",
                  variable=var, value=0)
green = Radiobutton(text="Green",
                    variable=var, value=1)
blue = Radiobutton(text="Blue",
                   variable=var, value=2)
button = Button(text="Изменить",
                command=change)
label = Label(width=20, height=10)
red.pack()
green.pack()
blue.pack()
button.pack()
label.pack()

root.mainloop()





# def clicked():
#     global button_show
#     global button_choose
#     global button_close
#     # button.destroy()
#     button_show = Button(window, text="Show", command=function_show, font='Arial 9 bold', bg='#de7e10', fg='white',
#                          relief=GROOVE)
#     button_show.place(x=150, y=100, width=100, height=30)
#     button_choose = Button(window, text="Choose", command=function_choose, font='Arial 9 bold', bg='#de7e10',
#                            fg='white',
#                            relief=GROOVE)
#     button_choose.place(x=150, y=160, width=100, height=30)
#     button_close = Button(window, text="Close", command=function_menu_off, font='Arial 9 bold', bg='#de7e10',
#                           fg='white',
#                           relief=GROOVE)
#     button_close.place(x=150, y=220, width=100, height=30)
