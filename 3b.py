from tkinter import *
import random


def game_quest(answer, quest):
    if quest == "If circle have got edges":
        if answer == 0:
            print('Brawo, jesteś super')
        else:
            print('To nic, spróbuj jeszcze raz')
    elif quest == "If circle have not got edges":
        if answer == 1:
            print('Brawo, jesteś super')
        else:
            print('To nic, spróbuj jeszcze raz')
    elif quest == "If square have got edges":
        if answer == 1:
            print('Brawo, jesteś super')
        else:
            print('To nic, spróbuj jeszcze raz')


app = Tk()
app.title('Interface')
app.geometry('250x100')

head_label = Label(app, text='Answer for question, clicked yes or no')
head_label.grid(row=1, column=1)

questions = ["If circle have got edges", "If circle have not got edges", "If square have got edges"]

quest_label = Label(app, text='There is show random question')
quest_label.grid(row=2, column=1)
quest = random.choice(questions)
quest_label.config(text=quest)

button1 = Button(app, text='Yes', command=lambda *args: game_quest(1, quest))
button1.grid(row=3, column=1)

button2 = Button(app, text='No', command=lambda *args: game_quest(0, quest))
button2.grid(row=3, column=2)

app.mainloop()
