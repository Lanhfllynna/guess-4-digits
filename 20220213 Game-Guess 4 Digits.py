#coding: utf-8

import tkinter as tk  #Library: tkinter
import tkinter.messagebox as tmsg #Library: tkinter.messagebox
import random as R


#Event Driven Function
def GuessGame():

    b=editbox1.get()
    if len(b) != 4:
        tmsg.showerror("ERROR!", "Please enter EXACTLY 4 digits~")
    elif len(b) == 4:
        if (b<"0") or (b>"9999"):
            tmsg.showerror("ERROR!", "Your input is not a number!")
        elif (b>="0") and (b<="9999"):
            tmsg.showinfo("YOUR GUESS",b)

            Hit = 0
            for i in range(4):
                if a[i] == int(b[i]):
                    Hit = Hit +1

            Blow = 0
            for i in range(4):
                for j in range(4):
                    if (a[i] != int(b[i])) and (a[j] != int(b[j])) and (a[i] == int(b[j])):
                        Blow = Blow +1
                        break
            if Hit != 4:
                recordbox.insert(tk.END, b + "--Hit:" + str(Hit) + "; Blow:" + str(Blow) + "\n")


            if Hit == 4:
                tmsg.showinfo("END GAME!","BINGO! YOU GUESS!")
                frame.destoy()
                                                       
#-----------------------------------------------------------------
#Generate 4 digit number randomly
a=[R.randint(0,9), R.randint(0,9), R.randint(0,9), R.randint(0,9)]


#Function: Tk()
frame= tk.Tk()
frame.geometry("800x400")
frame.title("Guess 4-Digit Number")

#Function: Label()
label1=tk.Label(frame,
                text="Please enter your guess:",
                font=("Helvetica",18),
                foreground="yellow",
                background="navy",
                width=20, height=3)
label1.place(x=30, y=50)


#Function: Entry()
editbox1=tk.Entry(frame,  
                  width=6,      
                  font=("Helvetica", 42),
                  fg="red",
                  bg="white") 
editbox1.place(x=250, y=50)


#Function: Button()
button1=tk.Button(frame,
                  text="Confirm!",
                  font=("Helvetica", 16),
                  fg="black",  
                  width=8, height=2,
                  command=GuessGame) 
button1.place(x=250, y=120)

#Function: Text()
recordbox = tk.Text(frame,
                    font=("Helvetica", 14,),
                    fg="black",
                    bg="white",
                    width=200, height=400)
recordbox.place(x=400,y=0)

frame.mainloop()


