from tkinter import *


def add():
    i = 0

    while i < 5:
        print(sentence.get())
        i += 1


app = Tk()
app.title('Interface')
app.geometry('250x100')

sentence_l = Label(app, text='Entry sentence')
sentence_l.grid(row=1, column=1)
sentence = Entry(app, fg='blue')
sentence.grid(row=1, column=2)

button1 = Button(app, text="OK", command=add)
button1.grid(row=3, column=1)

app.mainloop()
