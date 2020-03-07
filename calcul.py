from tkinter import *
from tkinter import ttk
import tkinter as ttk

valeur = 0
total = 0
o = 'n'
MsgC = ""
lasts="welcome to my first app"
laste=0
z=True
def effacer():
    global valeur
    global msg
    global MsgC
    global o
    MsgC=MsgC[:-1]
    valeur=valeur//10
    msg = Message(root, text=MsgC)
    msg.config(bg='#ffd76e', font=('neuton', 24, 'italic'), anchor="ne", width=500, foreground="navy")
    msg.grid(row=0, column=0, sticky="snew", ipadx=10, ipady=20, columnspan=4)


def reset():
    global valeur
    global msg
    global MsgC
    global o
    valeur = 0
    total = 0
    o = 'n'
    MsgC = ""
    lasts = "last value"
    laste = 0


def resett():
    msg = Message(root, text="0", fg="grey")
    msg.grid(row=0, column=0, sticky="snew", ipadx=10, ipady=20, columnspan=4)
    mes = Message(root, text="welcome to my first app ")
    mes.config(bg='#ffd76e', font=('neuton', 12, 'italic'), anchor="ne", width=500, foreground="navy")
    mes.grid(row=1, column=1, sticky="snew", ipadx=10, ipady=2, columnspan=2)
    reset()

def getvalue(x):
    global valeur
    global msg
    global MsgC
    global z
    if valeur == 0:
        valeur = x
    else:
        valeur = valeur * 10 + x
    MsgC = MsgC + str(x)
    msg = Message(root, text=MsgC)
    msg.config(bg='darksalmon', font=('neuton', 24, 'italic'),anchor="ne",width=500,foreground="navy")
    msg.grid(row=0, column=0, sticky="snew", ipadx=10, ipady=20, columnspan=4,rowspan=1)
    bef = ttk.Button(root, text="    efacer    ")
    bef.config(bg='turquoise', font=('neuton', 12, 'italic'), foreground="black")
    bef.grid(row=1, column=3, sticky="snew", columnspan=1)
    bef.config(command=lambda: effacer())
    br = ttk.Button(root, text="     reset     ")
    br.config(bg='turquoise', font=('neuton', 12, 'italic'), foreground="black")
    br.grid(row=1, column=0, sticky="snew", columnspan=1)
    br.config(command=lambda: resett())
    if z:
        mes = Message(root, text=lasts)
        mes.config(bg='#ffd76e', font=('neuton', 12, 'italic'), anchor="ne", width=500, foreground="navy")
        mes.grid(row=1, column=1, sticky="snew", ipadx=10, ipady=2, columnspan=2)


def check():
    global total
    global valeur
    if o == '+':
        total = total + valeur
    elif o == '-':
        total = total - int(valeur)
    elif o == '*':
        total = total * int(valeur)
    elif o == '/':
        total = total / int(valeur)
    elif o == 'n':
        total = int(valeur)


def addition():
    global MsgC
    global valeur
    global msg
    global total
    global o
    check()
    MsgC = MsgC + '+'
    valeur = 0
    msg = Message(root, text=MsgC)
    msg.config(bg='#ffd76e', font=('neuton', 24, 'italic'), anchor="ne", width=500, foreground="navy")
    msg.grid(row=0, column=0, sticky="snew", ipadx=10, ipady=20, columnspan=4)
    o = '+'


def soustraction():
    global MsgC
    global valeur
    global msg
    global total
    check()
    valeur = 0
    MsgC = MsgC + '-'
    msg = Message(root, text=MsgC)
    msg.config(bg='#ffd76e', font=('neuton', 24, 'italic'), anchor="ne", width=500, foreground="navy")
    msg.grid(row=0, column=0, sticky="snew", ipadx=10, ipady=20, columnspan=4)
    global o
    o = '-'


def multiplication():
    global valeur
    global msg
    global total
    global MsgC
    check()
    valeur = 0
    MsgC = MsgC + '*'
    msg = Message(root, text=MsgC)
    msg.config(bg='#ffd76e', font=('neuton', 24, 'italic'), anchor="ne", width=500, foreground="navy")
    msg.grid(row=0, column=0, sticky="snew", ipadx=10, ipady=20, columnspan=4)
    global o
    o = '*'


def division():
    global valeur
    global msg
    global total
    global MsgC
    check()
    valeur = 0
    MsgC = MsgC + '/ '
    msg = Message(root, text=MsgC)
    msg.config(bg='#ffd76e', font=('neuton', 24, 'italic'), anchor="ne", width=500, foreground="navy")
    msg.grid(row=0, column=0, sticky="snew", ipadx=10, ipady=20, columnspan=4)
    global o
    o = '/'



def lastvalue():
    global valeur
    global msg
    global total
    global MsgC
    global laste
    global lasts
    global x
    if valeur>0:
        MsgC=MsgC[:-len(str(valeur))]
    valeur = laste
    MsgC=MsgC+str(valeur)
    msg = Message(root, text=MsgC)
    msg.config(bg='#ffd76e', font=('neuton', 24, 'italic'), anchor="ne", width=500, foreground="navy")
    msg.grid(row=0, column=0, sticky="snew", ipadx=10, ipady=20, columnspan=4)






def calcul():
    global valeur
    global msg
    global total
    global MsgC
    global laste
    global lasts
    global z
    check()
    MsgC = MsgC + '=' + str(total)
    msg = Message(root, text=MsgC, width=500)
    msg.config(bg='#ffd76e', font=('neuton', 24, 'italic'), anchor="ne", width=500, foreground="navy")
    msg.grid(row=0, column=0, sticky="snew", ipadx=10, ipady=20, columnspan=4)
    laste=total
    lasts=str(laste)
    reset()
    bl = ttk.Button(root, text=lasts)
    bl.config(bg='turquoise', font=('neuton', 12, 'italic'), foreground="black")
    bl.grid(row=1, column=1, sticky="snew", columnspan=2)
    bl.config(command=lambda: lastvalue())
    z=False


root = Tk()

root.title("calculatrice")
#msg = Message(root, text="0", fg="grey")
#msg.grid(row=0, column=0, sticky="snew", ipadx=10, ipady=20, columnspan=4)



b0 = ttk.Button(root, text="0 ")
b0.config(bg='chocolate', font=('neuton', 15, 'italic'), foreground="white")
b0.grid(row=5, column=0, sticky="snew", ipadx=10, ipady=20, columnspan=2)
b0.config(command=lambda: getvalue(0))

b1 = ttk.Button(root, text="1")
b1.config(bg='chocolate', font=('neuton', 12, 'italic'), foreground="white")
b1.grid(row=4, column=0, sticky="snew", ipadx=10, ipady=20)
b1.config(command=lambda: getvalue(1))

b2 = ttk.Button(root, text="2 ")
b2.config(bg='chocolate', font=('neuton', 12, 'italic'), foreground="white")
b2.grid(row=4, column=1, sticky="snew", ipadx=10, ipady=20)
b2.config(command=lambda: getvalue(2))

b3 = ttk.Button(root, text="3")
b3.config(bg='chocolate', font=('neuton', 12, 'italic'), foreground="white")
b3.grid(row=4, column=2, sticky="snew", ipadx=10, ipady=20)
b3.config(command=lambda: getvalue(3))

b4 = ttk.Button(root, text="4 ")
b4.config(bg='chocolate', font=('neuton', 12, 'italic'), foreground="white")
b4.grid(row=3, column=0, sticky="snew", ipadx=10, ipady=20)
b4.config(command=lambda: getvalue(4))

b5 = ttk.Button(root, text="5")
b5.config(bg='chocolate', font=('neuton', 12, 'italic'), foreground="white")
b5.grid(row=3, column=1, sticky="snew", ipadx=10, ipady=20)
b5.config(command=lambda: getvalue(5))

b6 = ttk.Button(root, text="6 ")
b6.config(bg='chocolate', font=('neuton', 12, 'italic'), foreground="white")
b6.grid(row=3, column=2, sticky="snew", ipadx=10, ipady=20)
b6.config(command=lambda: getvalue(6))

b7 = ttk.Button(root, text="7")
b7.config(bg='chocolate', font=('neuton', 12, 'italic'), foreground="white")
b7.grid(row=2, column=0, sticky="snew", ipadx=10, ipady=20)
b7.config(command=lambda: getvalue(7))

b8 = ttk.Button(root, text="8 ")
b8.config(bg='chocolate', font=('neuton', 12, 'italic'), foreground="white")
b8.grid(row=2, column=1, sticky="snew", ipadx=10, ipady=20)
b8.config(command=lambda: getvalue(8))

b9 = ttk.Button(root, text="9")
b9.config(bg='chocolate', font=('neuton', 12, 'italic'), foreground="white")
b9.grid(row=2, column=2, sticky="snew", ipadx=10, ipady=20)
b9.config(command=lambda: getvalue(9))

ba = ttk.Button(root, text="+")
ba.config(bg='turquoise', font=('neuton', 12, 'italic'), foreground="black")
ba.grid(row=2, column=3, sticky="snew", ipadx=10, ipady=20)
ba.config(command=lambda: addition())

bs = ttk.Button(root, text="-")
bs.config(bg='turquoise', font=('neuton', 12, 'italic'), foreground="black")
bs.grid(row=3, column=3, sticky="snew", ipadx=10, ipady=20)
bs.config(command=lambda: soustraction())

bm = ttk.Button(root, text="*")
bm.config(bg='turquoise', font=('neuton', 12, 'italic'), foreground="black")
bm.grid(row=4, column=3, sticky="snew", ipadx=10, ipady=20)
bm.config(command=lambda: multiplication())

bd = ttk.Button(root, text="/")
bd.config(bg='turquoise', font=('neuton', 12, 'italic'), foreground="black")
bd.grid(row=5, column=3, sticky="snew", ipadx=10, ipady=20)
bd.config(command=lambda: division())

be = ttk.Button(root, text="=")
be.config(bg='turquoise', font=('neuton', 12, 'italic'), foreground="black")
be.grid(row=5, column=2, sticky="snew", ipadx=10, ipady=20)
be.config(command=lambda: calcul())




mes = Message(root, text="welcome to my first app ")
mes.config(bg='#ffd76e', font=('neuton', 12, 'italic'), anchor="ne", width=500, foreground="navy")
mes.grid(row=0, column=0, sticky="snew", ipadx=10, ipady=2, columnspan=4)


root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.rowconfigure(3,weight=1)
root.rowconfigure(4,weight=1)


root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)
root.columnconfigure(4,weight=1)



mainloop()
