from tkinter import *


def add():
    try:
        result = int(integer1.get()) + int(integer2.get())
        result_l.config(text='Result of action is: {}'.format(result))



app = Tk()
app.title('my app')
app.geometry('250x200')

Label(text='Entry first integer: ').grid(row=1, column=1)

integer1 = Entry(app, fg='blue')
integer1.grid(row=1, column=2)

Label(text='Entry second integer: ').grid(row=2, column=1)

integer2 = Entry(app, fg='blue')
integer2.grid(row=2, column=2)

Button(text='OK', command=add).grid(row=3, column=1)

result_l = Label(text='Place for result')
result_l.grid(row=3, column=2)

app.mainloop()
