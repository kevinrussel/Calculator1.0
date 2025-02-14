import tkinter as tk
## create the root.
root = tk.Tk()

## now We shall make the window pane size

root.geometry("500x400")
root.title("Calculator 1.0")

## now its time to make a text box.
text = tk.Text(height=3)
text.pack()

ButtonFrame = tk.Frame()

ButtonFrame.columnconfigure(0,weight= 1)
ButtonFrame.columnconfigure(1,weight= 1)
ButtonFrame.columnconfigure(2,weight= 1)


btn1 = tk.Button(ButtonFrame,text='1', font=('Ariel',18))
btn1.grid( row=0, column=0, sticky= tk.W+tk.E)


btn2 = tk.Button(ButtonFrame,text='2', font=('Ariel',18))
btn2.grid( row=0, column=1, sticky= tk.W+tk.E)

btn3 = tk.Button(ButtonFrame,text='3', font=('Ariel',18))
btn3.grid( row=0, column=2, sticky= tk.W+tk.E)

btn4 = tk.Button(ButtonFrame,text='4', font=('Ariel',18))
btn4.grid( row=1, column=0, sticky= tk.W+tk.E)

btn5 = tk.Button(ButtonFrame,text='5', font=('Ariel',18))
btn5.grid( row=1, column=1, sticky= tk.W+tk.E)

btn6 = tk.Button(ButtonFrame,text='6', font=('Ariel',18))
btn6.grid( row=1, column=2, sticky= tk.W+tk.E)

btn7 = tk.Button(ButtonFrame,text='7', font=('Ariel',18))
btn7.grid( row=2, column=0, sticky= tk.W+tk.E)

btn8 = tk.Button(ButtonFrame,text='8', font=('Ariel',18))
btn8.grid( row=2, column=1, sticky= tk.W+tk.E)

btn9 = tk.Button(ButtonFrame,text='9', font=('Ariel',18))
btn9.grid( row=2, column=2, sticky= tk.W+tk.E)

ButtonFrame.pack(fill="x")
root.mainloop();