from tkinter import *

app = Tk()
app.geometry('300x150')


def add():
    try:
        result = lambda int1, int2: int(int1) + int(int2)
        l_result.config(text='Result of action is : {}'.format(result(integer1.get(), integer2.get())))
    except ValueError:
        print('To nie jest cyfra!')


l1 = Label(app, text='Podaj pierwszą liczbę:')
l1.grid(row=1, column=1)
integer1 = Entry(app, fg='blue')
integer1.grid(row=1, column=2)

l2 = Label(app, text='Podaj drugą liczbę:')
l2.grid(row=2, column=1)
integer2 = Entry(app, fg='blue')
integer2.grid(row=2, column=2)

btn_ok = Button(app, text='OK', command=add)
btn_ok.grid(row=3, column=2)

l_result = Label(app, text='Result of action is: 0')
l_result.grid(row=4, column=2)

app.mainloop()
