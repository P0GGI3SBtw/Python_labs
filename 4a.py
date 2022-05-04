from tkinter import *


def add():
    result = int(var_a.get() + var_b.get())
    result_label.config(text='Result of action: {}'.format(result))


app = Tk()
app.geometry('200x300')
var_a = IntVar()
var_b = IntVar()

slide1 = Scale(app, from_=0, to=100, tickinterval=25, variable=var_a)
slide1.set(value=1)
slide1.grid(row=1, column=1)

slide2 = Scale(app, from_=0, to=100, variable=var_b)
slide2.set(value=1)
slide2.grid(row=1, column=2)

result_label = Label(app, text='Result of action: 0')
result_label.grid(row=2, column=1)

button_ok = Button(app, text='OK', fg='green', command=add)
button_ok.grid(row=3, column=1)

app.mainloop()
