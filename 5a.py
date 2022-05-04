from tkinter import *


def credit():
    q = 1 + p.get() / 100
    rata = (k.get() * q ** n.get() * (1 - q)) / (1 - q ** n.get())
    result_label.config(text='Rata branego kredytu: {}'.format(round(rata, 2)))


app = Tk()
app.geometry('500x200')
k = IntVar()
n = IntVar()
p = IntVar()


k_label = Label(text='Kwota udzielonego kredytu:')
k_label.grid(row=1, column=1)
slide1 = Scale(app, from_=1, to=1000000, variable=k)
slide1.set(value=1)
slide1.grid(row=2, column=1)

n_label = Label(text='Okres udzielonego kredytu w msc:')
n_label.grid(row=1, column=2)
slide2 = Scale(app, from_=1, to=12, tickinterval=1, variable=n)
slide2.set(value=1)
slide2.grid(row=2, column=2)

p_label = Label(text='Stopa procentowa:')
p_label.grid(row=1, column=3)
slide3 = Scale(app, from_=0, to=10, tickinterval=1, variable=p)
slide3.set(value=1)
slide3.grid(row=2, column=3)

button_ok = Button(app, text='Oblicz rate', bg='white', fg='green', command=credit)
button_ok.grid(row=3, column=1)

result_label = Label(text='Rata branego kredytu: 0')
result_label.grid(row=4, column=1)

app.mainloop()
