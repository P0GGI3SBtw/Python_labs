from tkinter import *


def divide():
    try:
        result = int(integer1.get()) / int(integer2.get())
        result_l.config(text='Result of action is: {}'.format(round(result, 2)))
    except ZeroDivisionError:
        result_l.config(text='Can not divide by 0')
    except Exception as e:
        result_l.config(text='Result of action is: 0')


app = Tk()
app.title('my app')
app.geometry('350x200')

Label(text='Entry first integer: ').grid(row=1, column=1)

integer1 = Entry(app, fg='blue')
integer1.grid(row=1, column=2)

Label(text='Entry second integer: ').grid(row=2, column=1)

integer2 = Entry(app, fg='blue')
integer2.grid(row=2, column=2)

Button_ok = Button(text='OK', command=divide)
Button_ok.grid(row=3, column=1)

result_l = Label(text='Place for result')
result_l.grid(row=3, column=2)

app.mainloop()
