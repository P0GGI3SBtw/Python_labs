from tkinter import *


def add():
    result = int(integer1.get()) + int(integer2.get())
    text_label.config(text='Result of action is: {}'.format(result))


app = Tk()
app.title('Interface')
app.geometry('250x100')

integer1l = Label(app, text='Entry first integer')
integer1l.grid(row=1, column=1)
integer1 = Entry(app, fg='blue')
integer1.grid(row=1, column=2)

integer2l = Label(app, text='Entry second integer')
integer2l.grid(row=2, column=1)
integer2 = Entry(app, fg='blue')
integer2.grid(row=2, column=2)
button1 = Button(app, text="OK", command=add)
button1.grid(row=3, column=1)

text_label = Label(app, text='Result of action is: 0')
text_label.grid(row=3, column=2)


app.mainloop()
