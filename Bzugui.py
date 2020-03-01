from tkinter import *



def output(event):
    minimal = float(1.2)
    low = float(1.375)
    average = float(1.55)
    high = float(1.725)
    veryhigh = float(1.9)

    if gender.get() == '1':  # Male gender
        try:
            bmr = 88.36 + (13.4 * weight.get()) + (4.8 * height.get()) - (5.7 * age.get())
        except UnboundLocalError:
            resultlabel.config(text="Введены не все данные!!! Попробуйте снова.")
        except:
            resultlabel.config(text="Введены неверные данные!!! Попробуйте снова.")
        bmr = round(bmr)
        if activity.get() == 1:
            result = minimal * bmr
        elif activity.get() == 2:
            result = low * bmr
        elif activity.get() == 3:
            result = average * bmr
        elif activity.get() == 4:
            result = high * bmr
        elif activity.get() == 5:
            result = veryhigh * bmr
        result = round(result)
        resultlabel.config(text="Результат: " + str(result) + " К.")
    if gender.get() == '2':  # Female gender
        try:
            bmr = 447.6 + (9.2 * weight.get()) + (3.1 * height.get()) - (4.3 * age.get())
        except UnboundLocalError:
            resultlabel.config(text="Введены не все данные!!! Попробуйте снова.")
        except:
            resultlabel.config(text="Введены неверные данные!!! Попробуйте снова.")
        bmr = round(bmr)
        if activity.get() == 1:
            result = minimal * bmr
        elif activity.get() == 2:
            result = low * bmr
        elif activity.get() == 3:
            result = average * bmr
        elif activity.get() == 4:
            result = high * bmr
        elif activity.get() == 5:
            result = veryhigh * bmr
        result = round(result)
        resultlabel.config(text="Рзультат: " + str(result) + " К.")

root = Tk()
root.title("Расчет суточного количества потребления калорий")
root.geometry("500x400")
root.resizable(False, False)  # Запрет изменения размеров окна.

description = str("Результат верен только для людей среднего телосложения !")

Info = Label(text=description, compound=BOTTOM, fg='blue', font=("Peignot", '16'))
gender = StringVar()
malegender = Radiobutton(text="Я МУЖИК", font=("Peignot", '16'), fg='#191970', cursor="man",
                         activebackground='blue', variable=gender, value=1)
femalegender = Radiobutton(text="Я ДАМА", font=("Peignot", '16'), fg='#191970', cursor='heart',
                           activebackground='#FF1493', variable=gender, value=2)


askweight = Label(text="ВЕС:", font=("Peignot", '13'), fg='#191970')
askheight = Label(text="РОСТ:", font=("Peignot", '13'), fg='#191970')
askage = Label(text="ВОЗРАСТ:", font=("Peignot", '13'), fg='#191970')

weight = IntVar()  # Переменная ввода веса
height = IntVar()  # Переменная ввода роста
age = IntVar()  # Переменная ввода возраста
activity = IntVar()  # Переменная выбора степени физической активности

entryweight = Entry(width='5', bd='3', fg='#0000CD', highlightthickness='1', textvariable=weight)
entryheight = Entry(width='5', bd='3', fg='#0000CD', highlightthickness='1', textvariable=height)
entryage = Entry(width='5', bd='3', fg='#0000CD', highlightthickness='1', textvariable=age)

activlabel = Label(text="Выберите степень физической активности ", font=("Peignot", '19'), fg='#191970')

minimum = Radiobutton(text="Минимальная", font=("Peignot", '14'), fg='#191970',
                      activebackground='#ADFF2F', variable=activity, value=1)
low = Radiobutton(text="Низкая", font=("Peignot", '14'), fg='#191970',
                  activebackground='lightblue', variable=activity, value=2)
average = Radiobutton(text="Средняя", font=("Peignot", '14'), fg='#191970',
                      activebackground='green', variable=activity, value=3)
high = Radiobutton(text="Высокая", font=("Peignot", '14'), fg='#191970',
                   activebackground='#C71585', variable=activity, value=4)
veryhigh = Radiobutton(text="Очень высокая", font=("Peignot", '14'), fg='#191970',
                       activebackground='red', variable=activity, value=5)

resultbutton = Button(root, text="ПОСЧИТАТЬ РЕЗУЛЬТАТ", width="45", bg='#32CD32',
                      bd='3', relief=GROOVE, overrelief=SUNKEN)
resultbutton.bind("<Button-1>", output)

resultlabel = Label(font=("Peignot", '15'), text="Результат: ")

Info.place(x=20, y=0)
malegender.place(x=95, y=25)
femalegender.place(x=290, y=25)
askweight.place(x=95, y=61)
entryweight.place(x=95, y=91)
askheight.place(x=200, y=61)
entryheight.place(x=200, y=91)
askage.place(x=310, y=61)
entryage.place(x=320, y=91)
activlabel.place(x=60, y=130)
minimum.place(x=100, y=170)
low.place(x=290, y=170)
average.place(x=100, y=210)
high.place(x=290, y=210)
veryhigh.place(x=195, y=250)
resultbutton.place(x=100, y=290)
resultlabel.place(x=100, y=330)
root.mainloop()

