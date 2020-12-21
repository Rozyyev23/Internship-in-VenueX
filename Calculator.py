from tkinter import *
from math import sqrt
import numpy as np
import traceback

def Linear (a1, b1):
    """Решает линейное уравнение"""
    x = -b1/a1
    text1 = "X равен: %s \n " % x
    return text1

def Quadratic (a2, b2, c2):
    """ Решает квадратное уравнение и выводит отформатированный ответ """
    # находим дискриминант
    D = b2*b2 - 4*a2*c2
    if D >= 0:
        x1 = (-b2 + sqrt(D)) / (2*a2)
        x2 = (-b2 - sqrt(D)) / (2*a2)
        text2 = "Дискриминант равен: %s \n X1 равен: %s \n X2 равен: %s \n" % (D, x1, x2)
    else:
        text2 = "Дискриминант равен: %s \n Функция не имеет решений" % D
    return text2

def Cubic (a3, b3, c3, d3):
    """ Решает кубическое уравнение и выводит отформатированный ответ """
    p = [a3, b3, c3, d3]
    q = np.roots(p)
    #out1 = float('{:.3f}'.format(q[0]))
    #out2 = float('{:.3f}'.format(q[1]))
    #out3 = float('{:.3f}'.format(q[2]))
    out1 = float(round(q[0], 2))
    out2 = float(round(q[1], 2))
    out3 = float(round(q[2], 2))
    text3 = " X1 равен: %s \n X2 равен: %s \n X3 равен: %s \n" % (out1, out2, out3)
    return text3

def Quartic (a2, b2, c2):
    """ Решает квадратное уравнение и выводит отформатированный ответ """
    # находим дискриминант
    D = b2*b2 - 4*a2*c2
    if D >= 0:
        x1 = sqrt((-b2 + sqrt(D)) / (2*a2))
        x2 = sqrt((-b2 - sqrt(D)) / (2*a2))
        text4 = "The discriminant is: %s \n X1 is:+- %s \n X2 is:+- %s \n" % (D, x1, x2)
    else:
        text4 = "The discriminant is: %s \n This equation has no solutions" % D
    return text4

def Linear_win():
    filewin = Toplevel(root)
    filewin.title("Линейное")

    def handler_Linear():
        """ передает функции inserter либо результат решения уравнения, либо сообщение о неверно введенных данных """
        try:
            # make sure that we entered correct values
            a1_val = float(a1.get())
            b1_val = float(b1.get())
            inserter(Linear(a1_val, b1_val))
        except ValueError:
            inserter("Перепроверьте введеность 2 цифр")

    def inserter(value):
        """ очищает поле для ввода и вставляет туда переданный ей аргумент value """
        output.delete("0.0", "end")
        output.insert("0.0", value)


    # выключаем возможность изменять окно
        filewin.resizable(width=False, height=False)

    # создаем рабочую область
    frame = Frame(filewin)
    frame.grid()

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=35, height=10)
    output.grid(row=5, columnspan=11)


    # поле для ввода первого аргумента уравнения (a1)
    # a1 = Entry(frame, width=3, state=DISABLED)
    a1 = Entry(frame, width=3)
    a1.grid(row=2, column=5, padx=(0, 0))

    # текст после первого аргумента
    a1_lab = Label(frame, text="X +").grid(row=2, column=6, padx=(0, 0))

    # поле для ввода второго аргумента уравнения (b1)
    b1 = Entry(frame, width=3)
    b1.grid(row=2, column=7)
    # текст после второго аргумента
    b1_lab = Label(frame, text="= 0").grid(row=2, column=8)

    # кнопка решить
    but = Button(frame, text="Решить", command=handler_Linear).grid(row=2, column=9, padx=(10, 10), pady=(5, 5))

def Quadratic_win():
    filewin = Toplevel(root)
    filewin.title("Квадратное")

    def handler_Quadratic():
        """ передает функции inserter либо результат решения уравнения, либо сообщение о неверно введенных данных """
        try:
            # make sure that we entered correct values
            a2_val = float(a2.get())
            b2_val = float(b2.get())
            c2_val = float(c2.get())
            inserter(Quadratic(a2_val, b2_val, c2_val))
        except ValueError:
            inserter("Проверьте введенность 3 цифр")
    def inserter(value):
        """ очищает поле для ввода и вставляет туда переданный ей аргумент value """
        output.delete("0.0", "end")
        output.insert("0.0", value)


    # выключаем возможность изменять окно
    filewin.resizable(width=False, height=False)

    # создаем рабочую область
    frame = Frame(filewin)
    frame.grid()

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=35, height=10)
    output.grid(row=5, columnspan=11)

    # поле для ввода первого аргумента уравнения (a2)
    a2 = Entry(frame, width=3)
    a2.grid(row=3, column=3, padx=(0, 0))

    # текст после первого аргумента
    a2_lab = Label(frame, text="X^2 +").grid(row=3, column=4, padx=(0, 0))

    # поле для ввода второго аргумента уравнения (b2)
    b2 = Entry(frame, width=3)
    b2.grid(row=3, column=5, padx=(0, 0))
    # текст после второго аргумента
    b2_lab = Label(frame, text="X +").grid(row=3, column=6, padx=(0, 0))

    # поле для ввода третьего аргумента уравнения (с2)
    c2 = Entry(frame, width=3)
    c2.grid(row=3, column=7, padx=(0, 0))
    # текст после третьего аргумента
    c2_lab = Label(frame, text="= 0").grid(row=3, column=8, padx=(0, 0))

    # кнопка решить
    but = Button(frame, text="Решить", command=handler_Quadratic).grid(row=3, column=9, padx=(10, 10), pady=(5, 5))

def Cubic_win():
    filewin = Toplevel(root)
    filewin.title("Кубическое")

    def handler_Cubic():
        """ передает функции inserter либо результат решения уравнения, либо сообщение о неверно введенных данных """
        try:
            # make sure that we entered correct values
            a3_val = float(a3.get())
            b3_val = float(b3.get())
            c3_val = float(c3.get())
            d3_val = float(d3.get())
            inserter(Cubic(a3_val, b3_val, c3_val, d3_val))
        except ValueError:
            inserter("Проверьте введенность 4 цифр")


    def inserter(value):
        """ очищает поле для ввода и вставляет туда переданный ей аргумент value """
        output.delete("0.0", "end")
        output.insert("0.0", value)

    # выключаем возможность изменять окно
        filewin.resizable(width=False, height=False)

    # создаем рабочую область
    frame = Frame(filewin)
    frame.grid()

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=35, height=10)
    output.grid(row=5, columnspan=11)

    # поле для ввода первого аргумента уравнения (a3)
    a3 = Entry(frame, width=3)
    a3.grid(row=4, column=1, padx=(10, 0))

    # текст после первого аргумента
    a3_lab = Label(frame, text="X^3 +").grid(row=4, column=2, padx=(0, 0))

    # поле для ввода второго аргумента уравнения (b3)
    b3 = Entry(frame, width=3)
    b3.grid(row=4, column=3, padx=(0, 0))
    # текст после второго аргумента
    b3_lab = Label(frame, text="X^2 +").grid(row=4, column=4, padx=(0, 0))

    # поле для ввода третьего аргумента уравнения (с3)
    c3 = Entry(frame, width=3)
    c3.grid(row=4, column=5, padx=(0, 0))
    # текст после третьего аргумента
    c3_lab = Label(frame, text="X + ").grid(row=4, column=6, padx=(0, 0))

    # поле для ввода третьего аргумента уравнения (d3)
    d3 = Entry(frame, width=3)
    d3.grid(row=4, column=7, padx=(0, 0))
    # текст после третьего аргумента
    d3_lab = Label(frame, text="= 0").grid(row=4, column=8, padx=(0, 0))

    # кнопка решить
    but = Button(frame, text="Решить", command=handler_Cubic).grid(row=4, column=9, padx=(10, 10), pady=(5, 5))

def Quartic_win():
    filewin = Toplevel(root)
    filewin.title("Биквадратное")

    def handler_Quartic():
        """ передает функции inserter либо результат решения уравнения, либо сообщение о неверно введенных данных """
        try:
            # make sure that we entered correct values
            a2_val = float(a2.get())
            b2_val = float(b2.get())
            c2_val = float(c2.get())
            inserter(Quadratic(a2_val, b2_val, c2_val))
        except ValueError:
            inserter("Проверьте введенность 3 цифр")
    def inserter(value):
        """ очищает поле для ввода и вставляет туда переданный ей аргумент value """
        output.delete("0.0", "end")
        output.insert("0.0", value)


    # выключаем возможность изменять окно
    filewin.resizable(width=False, height=False)

    # создаем рабочую область
    frame = Frame(filewin)
    frame.grid()

    # место для вывода решения уравнения
    output = Text(frame, bg="lightblue", font="Arial 12", width=35, height=10)
    output.grid(row=5, columnspan=11)

    # поле для ввода первого аргумента уравнения (a2)
    a2 = Entry(frame, width=3)
    a2.grid(row=3, column=3, padx=(0, 0))

    # текст после первого аргумента
    a2_lab = Label(frame, text="X^4 +").grid(row=3, column=4, padx=(0, 0))

    # поле для ввода второго аргумента уравнения (b2)
    b2 = Entry(frame, width=3)
    b2.grid(row=3, column=5, padx=(0, 0))
    # текст после второго аргумента
    b2_lab = Label(frame, text="X^2 +").grid(row=3, column=6, padx=(0, 0))

    # поле для ввода третьего аргумента уравнения (с2)
    c2 = Entry(frame, width=3)
    c2.grid(row=3, column=7, padx=(0, 0))
    # текст после третьего аргумента
    c2_lab = Label(frame, text="= 0").grid(row=3, column=8, padx=(0, 0))

    # кнопка решить
    but = Button(frame, text="Решить", command=handler_Quartic).grid(row=3, column=9, padx=(10, 10), pady=(5, 5))

root = Tk()
root.title("Калькулятор")
label = Label( root, text ="***Чтобы выбрать тип уравнения нажмите на меню*** \n   Линейное уравнение имеет вид: \n      ax+b=0 \n   Квадратичное уравнение имеет вид: \n      ax^2+bx+c=0 \n   Кубическое уравнение имеет вид: \n      ax^3+bx^2+cx+d=0", justify=LEFT)
label.pack()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Линейное", command=Linear_win)
filemenu.add_command(label="Квадратное", command=Quadratic_win)
filemenu.add_command(label="Кубическое", command=Cubic_win)
filemenu.add_command(label="Биквадратное", command=Quartic_win)

filemenu.add_separator()

filemenu.add_command(label="Выйти", command=root.quit)
menubar.add_cascade(label="Меню", menu=filemenu)



root.config(menu=menubar)

root.mainloop()