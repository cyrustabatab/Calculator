import tkinter


entry_font = ('Arial',40,'bold')
button_font = ('Arial',30,'normal')


window = tkinter.Tk()
window.title('Calculator')
window.configure(padx=20,pady=20)

def typed(value):
    
    if value != '=':
        entry_variable.set(entry_variable.get() + str(value))
    else:
        result = entry_variable.get()
        entry.delete(0,tkinter.END)
        entry.insert(0,str(eval(result))

    entry.icursor(tkinter.END)

def changed(*args):
     
    if len(entry_variable.get()) >= 10:
        entry_variable.set(entry_variable.get()[:-1])


def clear():

    entry.delete(0,tkinter.END)

entry_variable = tkinter.StringVar()

entry_variable.trace('w',changed)

entry = tkinter.Entry(font=entry_font,textvariable=entry_variable,width=10)
entry.focus_set()
entry.grid(row=0,column=0,columnspan=4)


button_7 = tkinter.Button(text="7",font=entry_font,command=lambda: typed(7))
button_7.grid(row=1,column=0,padx=5,pady=20)

button_8 = tkinter.Button(text="8",font=entry_font,command=lambda: typed(8))
button_8.grid(row=1,column=1,padx=5,pady=20)

button_9 = tkinter.Button(text="9",font=entry_font,command=lambda: typed(9))
button_9.grid(row=1,column=2,padx=5,pady=20)

button_divide = tkinter.Button(text="/",font=entry_font,command=lambda:typed('/'))
button_divide.grid(row=1,column=3,padx=5,pady=20)


button_4 = tkinter.Button(text="4",font=entry_font,command=lambda: typed(4))
button_4.grid(row=2,column=0,padx=5,pady=20)

button_5 = tkinter.Button(text="5",font=entry_font,command=lambda: typed(5))
button_5.grid(row=2,column=1,padx=5,pady=20)

button_6 = tkinter.Button(text="6",font=entry_font,command=lambda: typed(6))
button_6.grid(row=2,column=2,padx=5,pady=20)

button_multiply = tkinter.Button(text="x",font=entry_font,command=lambda: typed('*'))
button_multiply.grid(row=2,column=3,padx=5,pady=20)


button_1 = tkinter.Button(text="1",font=entry_font,command=lambda: typed(1))
button_1.grid(row=3,column=0,padx=5,pady=20)

button_2 = tkinter.Button(text="2",font=entry_font,command=lambda: typed(2))
button_2.grid(row=3,column=1,padx=5,pady=20)

button_3 = tkinter.Button(text="3",font=entry_font,command=lambda:typed(3))
button_3.grid(row=3,column=2,padx=5,pady=20)

button_subtract = tkinter.Button(text="-",font=entry_font,command=lambda:typed('-'))
button_subtract.grid(row=3,column=3)

button_0 = tkinter.Button(text="0",font=entry_font)
button_0.grid(row=4,column=0,padx=5,pady=20)

button_period = tkinter.Button(text=".",font=entry_font,command=lambda: typed('.'))
button_period.grid(row=4,column=1,padx=5,pady=20)

button_equal = tkinter.Button(text="=",font=entry_font,bg='blue',command=lambda: typed('='))
button_equal.grid(row=4,column=2,padx=5,pady=20)

button_addition = tkinter.Button(text="+",font=entry_font,command=lambda: typed('+'))
button_addition.grid(row=4,column=3)


clear_button = tkinter.Button(text="CLEAR",font=entry_font,command=clear)
clear_button.grid(row=5,column=0,columnspan=4)

window.mainloop()



