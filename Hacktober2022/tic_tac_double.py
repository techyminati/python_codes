from tkinter import *
import tkinter.messagebox
import tkinter
root = tkinter.Tk()
root.title("..... TiC _ TaC _ Toe .....")
root.geometry("500x500")
count=0
turn='x'
def print(event):
    global count
    global turn  
    if turn=='x':
        event["text"]='X' 
        turn = 'y' 
    elif turn=='y':
        event["text"]='0'
        turn='x'
    count=count+1   
    win()
def clearboard():
    global count
    button1["text"]=''
    button2["text"]=''
    button3["text"]=''
    button4["text"]=''
    button5["text"]=''
    button6["text"]=''
    button7["text"]=''
    button8["text"]=''    
    button9["text"]=''
    count=0
def win():
    isgameover=True
    if button1["text"]=='X' and button2["text"]=='X' and button3["text"]=='X':
        tkinter.messagebox.showinfo("Result","Player 'X' win")

    elif button1["text"]=='0' and button2["text"]=='0' and button3["text"]=='0':
        tkinter.messagebox.showinfo("Result","Player 'Y' win")
    
    elif button4["text"]=='X' and button5["text"]=='X' and button6["text"]=='X':
        tkinter.messagebox.showinfo("Result","Player 'X' win")

    elif button4=='0' and button5["text"]=='0' and button6["text"]=='0':
        tkinter.messagebox.showinfo("Result","Player 'Y' win")

    elif button7["text"]=='X' and button8["text"]=='X' and button9["text"]=='X':
        tkinter.messagebox.showinfo("Result","Player 'X' win")

    elif button7["text"]=='0' and button8["text"]=='0' and button9["text"]=='0':
        tkinter.messagebox.showinfo("Result","Player 'Y' win")  

    elif button1["text"]=='X' and button4["text"]=='X' and button7["text"]=='X':
        tkinter.messagebox.showinfo("Result","Player 'X' win")

    elif button1["text"]=='0' and button4["text"]=='0' and button7["text"]=='0':
        tkinter.messagebox.showinfo("Result","Player 'Y' win")

    elif button2["text"]=='X' and button5["text"]=='X' and button8["text"]=='X':
        tkinter.messagebox.showinfo("Result","Player 'X' win")

    elif button2["text"]=='0' and button5["text"]=='0' and button8["text"]=='0':
        tkinter.messagebox.showinfo("Result","Player 'Y' win")

    elif button3["text"]=='X' and button6["text"]=='X' and button9["text"]=='X':
        tkinter.messagebox.showinfo("Result","Player 'X' win")

    elif button3["text"]=='0' and button6["text"]=='0' and button9["text"]=='0':
        tkinter.messagebox.showinfo("Result","Player 'Y' win") 

    elif button1["text"]=='X' and button5["text"]=='X' and button9["text"]=='X':
        tkinter.messagebox.showinfo("Result","Player 'X' win")

    elif button1["text"]=='0' and button5["text"]=='0' and button9["text"]=='0':
        tkinter.messagebox.showinfo("Result","Player 'Y' win")

    elif button3["text"]=='X' and button5["text"]=='X' and button7["text"]=='X':
        tkinter.messagebox.showinfo("Result","Player 'X' win")

    elif button3["text"]=='0' and button5["text"]=='0' and button7["text"]=='0':
        tkinter.messagebox.showinfo("Result","Player 'Y' win")
    elif count==9:
        tkinter.messagebox.showinfo("Result","Match is Tie")
    else:
        isgameover=False
    if isgameover==True:
        clearboard()
lab1= Label(root,bg='yellow',text="THIS IS A TiC_TaC_Toe Game ",height=1)
lab1.grid(row=0)
lab2=Label(root,bg='yellow',text="player x = 'X'",font=20)
lab2.grid(row=1,column=2)
lab3=Label(root,bg='yellow',text="player Y = '0'",font=20)
lab3.grid(row=2,column=2)

button1=Button(root,text='',bg='green',width=4,height=2,font=("Arial",30),command=lambda:print(button1))
button1.grid(row=3,column=1)
button2=Button(root,text='',bg='green',width=4,height=2,font=("Arial",30),command=lambda:print(button2))
button2.grid(row=3,column=2)
button3=Button(root,text='',bg='green',width=4,height=2,font=("Arial",30),command=lambda:print(button3))
button3.grid(row=3,column=3)
button4=Button(root,text='',bg='green',width=4,height=2,font=("Arial",30),command=lambda:print(button4))
button4.grid(row=4, column=1)
button5=Button(root,text='',bg='green',width=4,height=2,font=("Arial",30),command=lambda:print(button5))
button5.grid(row=4, column=2)
button6=Button(root,text='',bg='green',width=4,height=2,font=("Arial",30),command=lambda:print(button6))
button6.grid(row=4, column=3)
button7=Button(root,text='',bg='green',width=4,height=2,font=("Arial",30),command=lambda:print(button7))
button7.grid(row=5, column=1)
button8=Button(root,text='',bg='green',width=4,height=2,font=("Arial",30),command=lambda:print(button8))
button8.grid(row=5, column=2)
button9=Button(root,text='',bg='green',width=4,height=2,font=("Arial",30),command=lambda:print(button9))
button9.grid(row=5, column=3)

root.mainloop()