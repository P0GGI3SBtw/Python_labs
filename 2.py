from tkinter import *
from tkinter.messagebox import showerror

app = Tk()
app.geometry('300x150')
app.title('My app')


def add():
    if type(value1) == type(value2):
        result = lambda val1, val2: val1 + val2
        l_result.config(text='Result of action is : {}'.format(result(value1, value2)))
    else:
        showerror('Box:', 'Podano inne typy danych')


value1 = 'abc'

value2 = 12

btn_ok = Button(app, text='OK', command=add)
btn_ok.grid(row=3, column=2)

l_result = Label(app, text='Result of action is: ')
l_result.grid(row=4, column=2)

app.mainloop()
