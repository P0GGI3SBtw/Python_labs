from tkinter import *


def name():
    print('Szymon')


def surname():
    print('Kołodziejski')


app = Tk()
app.title('Interface')
app.geometry('250x300')

button1 = Button(app, text="Name", command=name)
button1.grid(row=1, column=1)

button2 = Button(app, text="Surname", command=surname)
button2.grid(row=1, column=2)

app.mainloop()
