import tkinter as tk

font = ('Comic Sans MS', 20)

# function call
def onClick(event):
    global p
    b = event.widget
    text = b['text']

    if text == 'x':
        textField.insert('end', "*")
        return

    if text == '=':
        try:
            ex = textField.get()
            result = eval(ex)
            textField.delete(0, 'end')
            textField.insert(0, result)
        except Exception as e:
            showerror("Error", e)
        return

    textField.insert('end', text)

def clear():
    clear = textField.get()
    clear = clear[0:len(ex) - 1]
    textField.delete(0, 'end')
    textField.insert(0, clear)


def all_clear():
    textField.delete(0, 'end')

window = tk.Tk(className='Calculator')
window.geometry('310x200')

textField = tk.Entry(window,font = font,justify = 'center')
textField.grid(row=0,column=0,pady=10)

buttonFrame = tk.Frame(window)
buttonFrame.grid(padx=10)

number = 1
for i in range(3):
    for j in range(3):
        btn = tk.Button(buttonFrame,text=str(number),font = font,width=4)
        btn.grid(row=i, column=j)
        number = number + 1
        btn.bind('<Button-1>', onClick)

btn0 = tk.Button(buttonFrame,text='0',font = font,width=8)
btn0.grid(row=3,column= 0,columnspan = 2)  
btn_dot = tk.Button(buttonFrame,text='.',font = font,width=4)
btn_dot.grid(row=3,column= 2)

btn_clear   = tk.Button(buttonFrame,text='<--',font = font,width=4,command=clear)
btn_clear.grid(row=0,column= 3)
btn_AC      = tk.Button(buttonFrame,text='AC',font = font,width=4,command=all_clear)
btn_AC.grid(row=0,column= 4)

btn_add   = tk.Button(buttonFrame,text='+',font = font,width=4)
btn_add.grid(row=1,column= 3)
btn_sub   = tk.Button(buttonFrame,text='-',font = font,width=4)
btn_sub.grid(row=2,column= 3)

btn_mul   = tk.Button(buttonFrame,text='*',font = font,width=4)
btn_mul.grid(row=1,column= 4)
btn_div   = tk.Button(buttonFrame,text='/',font = font,width=4)
btn_div.grid(row=2,column= 4)

btn_equal = tk.Button(buttonFrame,text='=',font = font,width=9,)
btn_equal.grid(row=3,column= 3,columnspan = 2)

btn0.bind('<Button-1>', onClick)
btn_dot.bind('<Button-1>', onClick)
btn_add.bind('<Button-1>', onClick)
btn_sub.bind('<Button-1>', onClick)
btn_mul.bind('<Button-1>', onClick)
btn_div.bind('<Button-1>', onClick)
btn_equal.bind('<Button-1>', onClick)


window.mainloop()
