import tkinter as tk
from tkinter import *
from tkinter.constants import END
import tkinter.messagebox as mb

app = tk.Tk()
app.title('Stack Imitator')
app.geometry('450x500')
app.rowconfigure([0,1,2,3,4,5,6,7,8], minsize=50)

stack = []

def show_msg():
    res = mb.askyesno('action confirm', 'Do you want to choose '+ lbox.get(lbox.curselection()) +'?')
    if res == True:
        action()

def OnKeyPress(event):
    push()
    clean()

def clean():
    text.delete(0, END)

def push():
    element = text.get().strip()
    stack.append(element)

def show_stack():
    mb.showinfo('Display the Stack', str(stack[:]))

def action():
    if lbox.get(lbox.curselection()) == 'peek':
        if stack:
            mb.showinfo('Peek the stack', str(stack[-1]))
        if not stack:
            mb.showwarning('exception','You can\'t peek an empty stack!')
    if lbox.get(lbox.curselection()) == 'pop':
        if stack:
            stack.pop()
            mb.showinfo('pop action','Please inspect the stack for comparison')
        if not stack:
            mb.showwarning('exception','You can\'t pop an empty stack!')
    if lbox.get(lbox.curselection()) == 'get size':
        mb.showinfo('Get the stack size', str(len(stack)))  
    lbox.selection_clear(0,END)

f0 = tk.Frame(master=app)
f0.grid(column=1, row=0, sticky='w', padx=10, pady=10)
lb = tk.Label(f0, width=30, height=5, fg='green', text='This app is to imitate stack - \n an important data structure', \
    font=("Helvetica", 14))
lb.pack()

f1 = tk.Frame(master=app)
f1.grid(column=1, row=1, sticky='w', padx=10, pady=10)
lb = tk.Label(f1, text='Please push an element into the stack:', font='Rouge, 12', fg='black')
lb.pack(side=tk.LEFT)
text = tk.Entry(f1)
text.bind("<Return>", OnKeyPress)
status = tk.Label(anchor="w")
text.pack(side=tk.LEFT)

f3 = tk.Frame(master=app)
f3.grid(column=1, row=2)
btn = tk.Button(f3, text='Inspect the Stack', width = 20, bg='lightblue', command=show_stack)
btn.pack()

f2 = tk.Frame(master=app)
f2.grid(column=1, row=3, sticky='w', padx=10, pady=5)
lb = tk.Label(f2, text='Please choose an action to the stack: ', font='Rouge, 12', fg='black')
lb.pack(side=tk.LEFT)
lbox = Listbox(f2, height=3,fg='blue',font='Helvetica 12')
list_action = ['peek','pop','get size']
for i in list_action:
    lbox.insert(END,i)
lbox.pack()

f5 = tk.Frame(master=app)
f5.grid(column=1, row=4)
btn = tk.Button(f5, text='OK', width = 10, bg='pink', command=show_msg)
btn.pack()

# start the program
tk.mainloop()
