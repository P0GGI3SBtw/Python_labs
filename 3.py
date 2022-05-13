from tkinter.messagebox import showerror, showwarning
from tkinter import *

app = Tk()
app.title('My app')
app.geometry('300x150')


def operators():
    result = 0
    try:
        if var.get() == 0:
            result = int(integer1.get()) * int(integer2.get())
        elif var.get() == 1:
            result = int(integer1.get()) / int(integer2.get())

        label_result.config(text='Result of action is: {}'.format(round(result, 2)))
    except ZeroDivisionError:
        showerror('Error:', 'Can not divide by 0')
    except ValueError:
        showwarning('Warning:', 'Wrong input')


Label(text='Entry first integer:').grid(row=1, column=1)

integer1 = Entry(app, fg='green')
integer1.grid(row=1, column=2)

Label(text='Entry second integer:').grid(row=2, column=1)

integer2 = Entry(app, fg='green')
integer2.grid(row=2, column=2)

var = IntVar()

R1 = Radiobutton(app, text='*', variable=var, value=0)
R1.grid(row=1, column=3)
R2 = Radiobutton(app, text='/', variable=var, value=1)
R2.grid(row=2, column=3)

button_ok = Button(app, text='OK', fg='green', command=operators)
button_ok.grid(row=3, column=1)

label_result = Label(app, text='Result of action is: 0')
label_result.grid(row=4, column=1)

app.mainloop()
