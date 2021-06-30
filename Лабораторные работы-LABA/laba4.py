from tkinter import *

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x400')


def clicked():
    global button_show
    global button_choose
    global button_close
    btn.destroy()
    button_show = Button(window, text="Show", bg="#eb903b", fg="yellow", command=function_show, relief=GROOVE,
                         font='Arial 10 bold')
    button_show.place(relx=.5, rely=.4, anchor="c", height=30, width=100, bordermode=OUTSIDE)
    button_choose = Button(window, text="Choose", bg="#eb903b", fg="yellow", relief=GROOVE, font='Arial 10 bold',
                           command=function_chose)
    button_choose.place(relx=.5, rely=.2, anchor="c", height=30, width=100, bordermode=OUTSIDE)
    button_close = Button(window, text="Close", bg="#eb903b", fg="yellow", command=menu_off, relief=GROOVE,
                          font='Arial 10 bold')
    button_close.place(relx=.5, rely=.6, anchor="c", height=30, width=100, bordermode=OUTSIDE)


def menu_on():
    global btn
    btn = Button(window, text="Menu", bg="#eb903b", fg="yellow", command=clicked, relief=GROOVE, font='Arial 10 bold')
    btn.place(relx=.5, rely=.5, anchor="c", height=30, width=100, bordermode=OUTSIDE)


menu_on()


def menu_off():
    button_show.destroy()
    button_choose.destroy()
    button_close.destroy()

    menu_on()


def function_show():
    box = []
    if len(box) == 0:
        pass
    elif len(box) > 0:
        button_show.destroy()
        button_choose.destroy()
        button_close.destroy()
        pass


def function_chose():
    button_show.destroy()
    button_choose.destroy()
    button_close.destroy()
    label_show = Label(window, text="Привет", font='Arial 10old')
    label_show.place(relx=.5, rely=.2, anchor="c", bordermode=OUTSIDE)


window.mainloop()
