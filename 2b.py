from tkinter import *


def add():
    result = sentence1.get() + " " + sentence2.get()
    text_label.config(text='Full sentence is: {}'.format(result))


app = Tk()
app.title('Interface')
app.geometry('350x100')

sentence1l = Label(app, text='Entry first sentence')
sentence1l.grid(row=1, column=1)
sentence1 = Entry(app, fg='blue')
sentence1.grid(row=1, column=2)

sentence2l = Label(app, text='Entry second sentence')
sentence2l.grid(row=2, column=1)
sentence2 = Entry(app, fg='red')
sentence2.grid(row=2, column=2)

button1 = Button(app, text="OK", command=add)
button1.grid(row=3, column=1)

text_label = Label(app, text='Full sentence is: NULL')
text_label.grid(row=3, column=2)


app.mainloop()
