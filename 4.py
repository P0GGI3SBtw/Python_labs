from tkinter.messagebox import showerror
from tkinter import *

app = Tk()
app.geometry('300x150')
app.title('My app')


def operators():
    result = 0
    try:
        result = int(integer1.get()) / int(integer2.get())
        label_result.config(text='Result of action is: {}'.format(result))
    except ZeroDivisionError:
        showerror('Box:', 'Nie można dzielić przez 0')
    finally:
        label_result.config(text='Result of action is: {}'.format(result))


l1 = Label(text='Podaj pierwszą liczbę:')
l1.grid(row=1, column=1)
integer1 = Entry(app, fg='green')
integer1.grid(row=1, column=2)

l2 = Label(text='Podaj drugą liczbę:')
l2.grid(row=2, column=1)
integer2 = Entry(app, fg='green')
integer2.grid(row=2, column=2)

button_ok = Button(app, text='OK', fg='green', command=operators)
button_ok.grid(row=3, column=1)

label_result = Label(app, text='Result of action is: 0')
label_result.grid(row=4, column=1)

app.mainloop()
