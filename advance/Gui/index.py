from tkinter import *


window = Tk()
window.geometry("400x400")
window.minsize(400, 400)
window.maxsize(400, 400)

window.title = "Question from"
window.config(background='#fcb353')

frame = Frame(window)
frame.pack()

question = Label(frame, text="what are you doing?")
question.pack()
btnA = Button(frame, text='A. ...')
btnA.pack(side=TOP)

btnB = Button(frame, text='B. ...')
btnB.pack(side=TOP)

btnC = Button(frame, text='C. ...')
btnC.pack(side=TOP)

btnD = Button(frame, text='D. ...')
btnD.pack(side=TOP)


window.mainloop()
