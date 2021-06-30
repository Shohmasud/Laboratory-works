# Лабораторная работа 6
# вариант-4
# Разработайте приложение «Книги».
# Разработайте структуру xml-файла для хранения таких данных, как название, авторы, жанр, год, количество страниц, тираж, отпечатано листов.
# Предусмотрите возможность сортировки данных по автору книги и поиска данных по названию  и по жанру.


from tkinter import *
import csv
import tkinter.ttk as ttk
import tkinter as tk

from tkinter import filedialog as fd

window = tk.Tk()
box = []
sr = []


class App:
    def __init__(self, path):
        self.Tk = tk.Tk
        self.path = path
        self.path.title("Добро пожаловать в приложение Python")
        self.path.config(bg="#d7d8d9")
        self.path.geometry("1420x660+250+150")
        self.resalt = []
        self.f1()
        b1 = Button(window, text="Открыть", command=self.insert_text, width=15)
        b1.place(x=550, y=500)

    def f_button(self):
        get_search = self.text_box_text.get()
        box = []
        with open(f'D:\pythonn_filee\csv.csv', newline='', encoding='utf8') as File:
            reader = csv.reader(File)
            for row in reader:
                box.append(row)
        st = 0
        if self.var.get() == 0:
            st = 0
        elif self.var.get() == 1:
            st = 1
        elif self.var.get() == 2:
            st = 2
        i = 0
        for words in box:
            if get_search in words:
                self.resalt.append(words)
                if i == 0:
                    with open(f'D:\pythonn_filee\csv2.csv', 'w', encoding='utf8', newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow(words)
                if i > 0:
                    with open(f'D:\pythonn_filee\csv2.csv', 'a', encoding='utf8', newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow(words)
        self.f3()

        columns2 = ("#1", "#2", "#3", "#4", "#5", '#6', '#7')
        self.tree2 = ttk.Treeview(self.path, show="headings", columns=columns2)
        self.tree2.heading("#1", text="Название книги")
        self.tree2.heading("#2", text="Автор")
        self.tree2.heading("#3", text="Жанр")
        self.tree2.heading("#4", text="Год")
        self.tree2.heading("#5", text="Страницы")
        self.tree2.heading("#6", text="Тиражи")
        self.tree2.heading("#7", text="Отпечатано страниц")
        ysb2 = ttk.Scrollbar(self.path, orient=tk.VERTICAL, command=self.tree2.yview)
        self.tree2.configure(yscroll=ysb2.set)

        with open(f"../csv2.csv", newline="", encoding='utf8') as f2:
            for contact2 in csv.reader(f2):
                self.tree2.insert("", tk.END, values=contact2)
        self.tree2.bind("<<TreeviewSelect>>", self.print_selection)
        #
        self.tree2.grid(row=0, column=0)
        ysb2.grid(row=0, column=1, sticky=tk.N + tk.S)
        self.tree2.rowconfigure(0, weight=2)
        self.tree2.columnconfigure(0, weight=1)
        self.f_res()

    def f3(self):
        columns2 = ("#1", "#2", "#3", "#4", "#5", '#6', '#7')
        self.tree2 = ttk.Treeview(self.path, show="headings", columns=columns2)
        self.tree2.heading("#1", text="Название книги")
        self.tree2.heading("#2", text="Автор")
        self.tree2.heading("#3", text="Жанр")
        self.tree2.heading("#4", text="Год")
        self.tree2.heading("#5", text="Страницы")
        self.tree2.heading("#6", text="Тиражи")
        self.tree2.heading("#7", text="Отпечатано страниц")
        ysb2 = ttk.Scrollbar(self.path, orient=tk.VERTICAL, command=self.tree2.yview)
        self.tree2.configure(yscroll=ysb2.set)

        with open(f"../csv2.csv", newline="", encoding='utf8') as f2:
            for contact2 in csv.reader(f2):
                self.tree2.insert("", tk.END, values=contact2)
        self.tree2.bind("<<TreeviewSelect>>", self.print_selection)
        #
        self.tree2.grid(row=0, column=0)
        ysb2.grid(row=0, column=1, sticky=tk.N + tk.S)
        self.tree2.rowconfigure(0, weight=2)
        self.tree2.columnconfigure(0, weight=1)
        self.f_res()

    def insert_text(self):
        self.file_name = fd.askopenfilename()
        f = open(self.file_name)
        f.close()
        self.f2()

    def f1(self):
        columns1 = ("#1", "#2", "#3", "#4", "#5", '#6', '#7')
        self.tree1 = ttk.Treeview(self.path, show="headings", columns=columns1)
        self.tree1.heading("#1", text="Название книги")
        self.tree1.heading("#2", text="Автор")
        self.tree1.heading("#3", text="Жанр")
        self.tree1.heading("#4", text="Год")
        self.tree1.heading("#5", text="Страницы")
        self.tree1.heading("#6", text="Тиражи")
        self.tree1.heading("#7", text="Отпечатано страниц")
        ysb1 = ttk.Scrollbar(self.path, orient=tk.VERTICAL, command=self.tree1.yview)
        self.tree1.configure(yscroll=ysb1.set)

        # with open(f"../pythonn_filee/csv.csv", newline="", encoding='utf8') as f1:
        #     for contact1 in csv.reader(f1):
        #         self.tree1.insert("", tk.END, values=contact1)
        self.tree1.bind("<<TreeviewSelect>>", self.print_selection)
        #
        self.tree1.grid(row=0, column=0)
        ysb1.grid(row=0, column=1, sticky=tk.N + tk.S)
        self.tree1.rowconfigure(0, weight=2)
        self.tree1.columnconfigure(0, weight=1)
        self.f_res()

    def f2(self):
        columns = ("#1", "#2", "#3", "#4", "#5", '#6', '#7')
        self.tree = ttk.Treeview(self.path, show="headings", columns=columns)
        self.tree.heading("#1", text="Название книги")
        self.tree.heading("#2", text="Автор")
        self.tree.heading("#3", text="Жанр")
        self.tree.heading("#4", text="Год")
        self.tree.heading("#5", text="Страницы")
        self.tree.heading("#6", text="Тиражи")
        self.tree.heading("#7", text="Отпечатано страниц")
        ysb = ttk.Scrollbar(self.path, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=ysb.set)

        with open(f"{self.file_name}", newline="", encoding='utf8') as f:
            for contact in csv.reader(f):
                self.tree.insert("", tk.END, values=contact)
        self.tree.bind("<<TreeviewSelect>>", self.print_selection)

        self.tree.grid(row=0, column=0)
        ysb.grid(row=0, column=1, sticky=tk.N + tk.S)
        self.tree.rowconfigure(0, weight=2)
        self.tree.columnconfigure(0, weight=1)

    def print_selection(self, event):
        for selection in self.tree.selection():
            item = self.tree.item(selection)
            last_name, first_name, email = item["values"][0:7]
            text = "Выбор: {}, {} <{}>"
            print(text.format(last_name, first_name, email))

    def f_res(self):
        self.text_box_text = tk.Entry(width=50)
        self.text_box_text.place(x=150, y=400)

        self.var = tk.IntVar()
        self.var.set(1)
        self.red = tk.Radiobutton(self.path, text="Автору",
                                  variable=self.var, value=0, font='Arial 10 bold')
        self.green = tk.Radiobutton(self.path, text="Жанру",
                                    variable=self.var, value=1, font='Arial 10 bold')
        self.blue = tk.Radiobutton(self.path, text="Названию",
                                   variable=self.var, value=2, font='Arial 10 bold')
        self.button = tk.Button(self.path, text="Поиск", command=self.f_button,
                                font='Arial 10 ', width=10)

        self.red.place(x=550, y=350)
        self.green.place(x=550, y=400)
        self.blue.place(x=550, y=450)
        self.button.place(x=365, y=420)


if __name__ == "__main__":
    app = App(window)
    window.mainloop()
    print(sr)
