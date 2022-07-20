from tkinter import *
from tkinter import messagebox
import tkinter


# Create the window
root = Tk()
root.iconbitmap("favicon.ico")
root.title("TiC Tac ToE")
root.resizable(False, False)

count = 0
click = True

photo_O = PhotoImage(file="O.png")
photo_X = PhotoImage(file="x.png")


Btn1 = StringVar()
Btn2 = StringVar()
Btn3 = StringVar()
Btn4 = StringVar()
Btn5 = StringVar()
Btn6 = StringVar()
Btn7 = StringVar()
Btn8 = StringVar()
Btn9 = StringVar()

def create_menu_bar():
    global click
    menubar = Menu(root)
    menubar.add_command(label="Restart", command=Restart)
    menubar.add_command(label = "Exit", command=lambda : root.destroy())
    menubar.add_command(label="Remember : X go first! ")
    root.config(menu=menubar)

def check_win():
    global click, count
    if (Btn1.get() == "X" and Btn2.get() == "X" and Btn3.get() == "X" or
    Btn4.get() == "X" and Btn5.get() == "X" and Btn6.get() == "X" or
    Btn7.get() == "X" and Btn8.get() == "X" and Btn9.get() == "X" or
    Btn1.get() == "X" and Btn5.get() == "X" and Btn9.get() == "X" or
    Btn3.get() == "X" and Btn5.get() == "X" and Btn7.get() == "X" or
    Btn1.get() == "X" and Btn4.get() == "X" and Btn7.get() == "X" or
    Btn3.get() == "X" and Btn6.get() == "X" and Btn9.get() == "X"):
        tkinter.messagebox.showinfo("Tic Tac Toe", "X wins!")
        count = 0
        clear()
    elif (Btn1.get() == "O" and Btn2.get() == "O" and Btn3.get() == "O" or
    Btn4.get() == "O" and Btn5.get() == "O" and Btn6.get() == "O" or
    Btn7.get() == "O" and Btn8.get() == "O" and Btn9.get() == "O" or
    Btn1.get() == "O" and Btn5.get() == "O" and Btn9.get() == "O" or
    Btn3.get() == "O" and Btn5.get() == "O" and Btn7.get() == "O" or
    Btn1.get() == "O" and Btn4.get() == "O" and Btn7.get() == "O" or
    Btn3.get() == "O" and Btn6.get() == "O" and Btn9.get() == "O"):
        tkinter.messagebox.showinfo("Tic Tac Toe", "O wins!")
        count = 0
        clear()
    elif (count == 9):
        tkinter.messagebox.showinfo("Tic Tac Toe", "Tie Game!")
        click = True
        count = 0
        clear()

def Restart():
    global click
    click = True
    play()

def clear():
    Btn1.set("")
    Btn2.set("")
    Btn3.set("")
    Btn4.set("")
    Btn5.set("")
    Btn6.set("")
    Btn7.set("")
    Btn8.set("")
    Btn9.set("")

def play():
    create_menu_bar()

    Button1 = Button(root, height=9, width=19, bd=.5, relief="ridge", bg="#ffffff", textvariable=Btn1, command=lambda:press(1,0,0))
    Button2 = Button(root, height=9, width=19, bd=.5, relief="ridge", bg="#ffffff", textvariable=Btn2, command=lambda:press(2,0,1))
    Button3 = Button(root, height=9, width=19, bd=.5, relief="ridge", bg="#ffffff", textvariable=Btn3, command=lambda:press(3,0,2))
    Button4 = Button(root, height=9, width=19, bd=.5, relief="ridge", bg="#ffffff", textvariable=Btn4, command=lambda:press(4,1,0))
    Button5 = Button(root, height=9, width=19, bd=.5, relief="ridge", bg="#ffffff", textvariable=Btn5, command=lambda:press(5,1,1))
    Button6 = Button(root, height=9, width=19, bd=.5, relief="ridge", bg="#ffffff", textvariable=Btn6, command=lambda:press(6,1,2))
    Button7 = Button(root, height=9, width=19, bd=.5, relief="ridge", bg="#ffffff", textvariable=Btn7, command=lambda:press(7,2,0))
    Button8 = Button(root, height=9, width=19, bd=.5, relief="ridge", bg="#ffffff", textvariable=Btn8, command=lambda:press(8,2,1))
    Button9 = Button(root, height=9, width=19, bd=.5, relief="ridge", bg="#ffffff", textvariable=Btn9, command=lambda:press(9,2,2))
    
    Button1.grid( row=0, column=0)
    Button2.grid( row=0, column=1)
    Button3.grid( row=0, column=2)
    Button4.grid( row=1, column=0)
    Button5.grid( row=1, column=1)
    Button6.grid( row=1, column=2)
    Button7.grid( row=2, column=0)
    Button8.grid( row=2, column=1)
    Button9.grid( row=2, column=2)

def press(num, r, c):
    global count
    global click 
    if click == True:
        labelPhoto = Label(root, image = photo_X)
        labelPhoto.grid(row=r,column=c)
        if num == 1 :
            Btn1.set("X")
        if num == 2 :
            Btn2.set("X")
        if num == 3 :
            Btn3.set("X")
        if num == 4 :
            Btn4.set("X")
        if num == 5 :
            Btn5.set("X")
        if num == 6 :
            Btn6.set("X")
        if num == 7 :
            Btn7.set("X")
        if num == 8 :
            Btn8.set("X")
        if num == 9 :
            Btn9.set("X")
        count+= 1
        click = False
        check_win()
    else:
        labelPhoto = Label(root, image=photo_O)
        labelPhoto.grid(row=r, column=c)
        if num == 1 :
            Btn1.set("O")
        if num == 2 :
            Btn2.set("O")
        if num == 3 :
            Btn3.set("O")
        if num == 4 :
            Btn4.set("O")
        if num == 5 :
            Btn5.set("O")
        if num == 6 :
            Btn6.set("O")
        if num == 7 :
            Btn7.set("O")
        if num == 8 :
            Btn8.set("O")
        if num == 9 :
            Btn9.set("O")
        count+= 1
        click = True
        check_win() 

play()
mainloop()