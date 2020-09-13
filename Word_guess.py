from tkinter import *
from random import *

win = Tk()

l1 = Label(win, text="Enter your guess: ")
l1.grid(row=0, column=0)

e1 = Entry(win, width=3, borderwidth=3)
e1.grid(row=0, column=1)

words = ["Planet", "Football", "Cricket", "Ant", "Galaxy", "Earth", "Horse", "Grass"]
word_secret = words[randint(0, 7)]

if len(word_secret) == 3:
    e1 = Entry(win, width=3, borderwidth=3)
    e1.grid(row=0, column=1)

    e2 = Entry(win, width=3, borderwidth=3)
    e2.grid(row=0, column=2)

    e3 = Entry(win, width=3, borderwidth=3)
    e3.grid(row=0, column=3) 

elif len(word_secret) == 5:
    e1 = Entry(win, width=3, borderwidth=3)
    e1.grid(row=0, column=1)

    e2 = Entry(win, width=3, borderwidth=3)
    e2.grid(row=0, column=2)

    e3 = Entry(win, width=3, borderwidth=3)
    e3.grid(row=0, column=3)

    e4 = Entry(win, width=3, borderwidth=3)
    e4.grid(row=0, column=4)

    e5 = Entry(win, width=3, borderwidth=3)
    e5.grid(row=0, column=5)                       

elif len(word_secret) == 6:
    e1 = Entry(win, width=3, borderwidth=3)
    e1.grid(row=0, column=1)

    e2 = Entry(win, width=3, borderwidth=3)
    e2.grid(row=0, column=2)

    e3 = Entry(win, width=3, borderwidth=3)
    e3.grid(row=0, column=3)

    e4 = Entry(win, width=3, borderwidth=3)
    e4.grid(row=0, column=4)

    e5 = Entry(win, width=3, borderwidth=3)
    e5.grid(row=0, column=5)

    e6 = Entry(win, width=3, borderwidth=3)
    e6.grid(row=0, column=6) 

elif len(word_secret) == 7:
    e1 = Entry(win, width=3, borderwidth=3)
    e1.grid(row=0, column=1)

    e2 = Entry(win, width=3, borderwidth=3)
    e2.grid(row=0, column=2)

    e3 = Entry(win, width=3, borderwidth=3)
    e3.grid(row=0, column=3)

    e4 = Entry(win, width=3, borderwidth=3)
    e4.grid(row=0, column=4)

    e5 = Entry(win, width=3, borderwidth=3)
    e5.grid(row=0, column=5)

    e6 = Entry(win, width=3, borderwidth=3)
    e6.grid(row=0, column=6)

    e7 = Entry(win, width=3, borderwidth=3)
    e7.grid(row=0, column=7)           

elif len(word_secret) == 8:
    e1 = Entry(win, width=3, borderwidth=3)
    e1.grid(row=0, column=1)

    e2 = Entry(win, width=3, borderwidth=3)
    e2.grid(row=0, column=2)

    e3 = Entry(win, width=3, borderwidth=3)
    e3.grid(row=0, column=3)

    e4 = Entry(win, width=3, borderwidth=3)
    e4.grid(row=0, column=4)

    e5 = Entry(win, width=3, borderwidth=3)
    e5.grid(row=0, column=5)

    e6 = Entry(win, width=3, borderwidth=3)
    e6.grid(row=0, column=6)

    e7 = Entry(win, width=3, borderwidth=3)
    e7.grid(row=0, column=7)

    e8 = Entry(win, width=3, borderwidth=3)
    e8.grid(row=0, column=8)    

def click(letter):
    if e1.get() == "":
        e1.insert(0, letter)
    elif e2.get() == "":
        e2.insert(0, letter)    
    elif e3.get() == "":
        e3.insert(0, letter)
    elif e4.get() == "":
        e4.insert(0, letter)
    elif e5.get() == "":
        e5.insert(0, letter) 
    elif e6.get() == "":
        e6.insert(0, letter) 
    elif e7.get() == "":
        e7.insert(0, letter) 
    elif e8.get() == "":
        e8.insert(0, letter)
    else:
        ""
  
    if len(word_secret) == 3:
        if e1.get().lower() == word_secret.lower()[0]:
            e1["state"] = DISABLED
            e1["bg"] = "blue"                           
        else:
            ""
        if e2.get().lower() == word_secret.lower()[1]:
            e2["state"] = DISABLED
            e2.bg = "blue"       
        else:
            ""            
        if e3.get().lower() == word_secret.lower()[2]:
            e3["state"] = DISABLED
            e3.bg = "blue"       
        else:
            ""
    elif len(word_secret) == 5:
        if e1.get().lower() == word_secret.lower()[0]:
            e1["state"] = DISABLED
            e1["bg"] = "blue"
        else:
            ""
        if e2.get().lower() == word_secret.lower()[1]:
            e2["state"] = DISABLED
            e2.bg = "blue"       
        else:
            ""            
        if e3.get().lower() == word_secret.lower()[2]:
            e3["state"] = DISABLED
            e3.bg = "blue"       
        else:
            ""
        if e4.get().lower() == word_secret.lower()[3]:
            e4["state"] = DISABLED
            e4.bg = "blue"
        else:
            "" 
        if e5.get().lower() == word_secret.lower()[4]:
            e5["state"] = DISABLED
            e5.bg = "blue"
        else:
            ""

    elif len(word_secret) == 6:
        if e1.get().lower() == word_secret.lower()[0]:
            e1["state"] = DISABLED
            e1["bg"] = "blue"
        else:
            ""
        if e2.get().lower() == word_secret.lower()[1]:
            e2["state"] = DISABLED
            e2.bg = "blue"       
        else:
            ""            
        if e3.get().lower() == word_secret.lower()[2]:
            e3["state"] = DISABLED
            e3.bg = "blue"       
        else:
            ""
        if e4.get().lower() == word_secret.lower()[3]:
            e4["state"] = DISABLED
            e4.bg = "blue"
        else:
            "" 
        if e5.get().lower() == word_secret.lower()[4]:
            e5["state"] = DISABLED
            e5.bg = "blue"
        else:
            ""
        if e6.get().lower() == word_secret.lower()[5]:
            e6["state"] = DISABLED
            e6.bg = "blue"
        else:
            ""

    elif len(word_secret) == 7:
        if e1.get().lower() == word_secret.lower()[0]:
            e1["state"] = DISABLED
            e1.bg = "blue"
        else:
            ""
        if e2.get().lower() == word_secret.lower()[1]:
            e2["state"] = DISABLED
            e2.bg = "blue"       
        else:
            ""            
        if e3.get().lower() == word_secret.lower()[2]:
            e3["state"] = DISABLED
            e3.bg = "blue"       
        else:
            ""
        if e4.get().lower() == word_secret.lower()[3]:
            e4["state"] = DISABLED
            e4.bg = "blue"
        else:
            "" 
        if e5.get().lower() == word_secret.lower()[4]:
            e5["state"] = DISABLED
            e5.bg = "blue"
        else:
            ""
        if e6.get().lower() == word_secret.lower()[5]:
            e6["state"] = DISABLED
            e6.bg = "blue"
        else:
            ""
        if e7.get().lower() == word_secret.lower()[6]:
            e7["state"] = DISABLED
            e7.bg = "blue"
        else:
            ""

    elif len(word_secret) == 8:
        if e1.get().lower() == word_secret.lower()[0]:
            e1["state"] = DISABLED
            e1["bg"] = "blue"
        else:
            ""
        if e2.get().lower() == word_secret.lower()[1]:
            e2["state"] = DISABLED
            e2.bg = "blue"       
        else:
            ""            
        if e3.get().lower() == word_secret.lower()[2]:
            e3["state"] = DISABLED
            e3.bg = "blue"       
        else:
            ""
        if e4.get().lower() == word_secret.lower()[3]:
            e4["state"] = DISABLED
            e4.bg = "blue"
        else:
            "" 
        if e5.get().lower() == word_secret.lower()[4]:
            e5["state"] = DISABLED
            e5.bg = "blue"
        else:
            ""
        if e6.get().lower() == word_secret.lower()[5]:
            e6["state"] = DISABLED
            e6.bg = "blue"
        else:
            ""
        if e7.get().lower() == word_secret.lower()[6]:
            e7["state"] = DISABLED
            e7.bg = "blue"
        else:
            ""
        if e8.get().lower() == word_secret.lower()[7]:
            e8["state"] = DISABLED
            e8.bg = "blue"       
        else:
            ""
    else:
        ""                      



def hint():
    if word_secret == "Ant":
        l2 = Label(win, text="It's an insect        ", fg="red")
        l2.grid(row=6, column=1)
    elif word_secret == "Planet":
        l2 = Label(win, text="Its is a Planet       ", fg="red")    
        l2.grid(row=6, column=1)
    elif word_secret == "Football":
        l2 = Label(win, text="It's is a sport       ", fg="red")
        l2.grid(row=6, column=1) 
    elif word_secret == "Cricket":
        l2 = Label(win, text="It's is a sport       ", fg="red")
        l2.grid(row=6, column=1)
    elif word_secret == "Galaxy":
        l2 = Label(win, text="It's is in universe   ", fg="red")
        l2.grid(row=6, column=1) 
    elif word_secret == "Earth":
        l2 = Label(win, text="It's is where you live", fg="red")
        l2.grid(row=6, column=1)
    elif word_secret == "Horse":
        l2 = Label(win, text="It's is an animal      ", fg="red")
        l2.grid(row=6, column=1)
    elif word_secret == "Grass":
        l2 = Label(win, text="It is what you find in backyard", fg="red")
        l2.grid(row=6, column=1)                      



b1 = Button(win, text="A", command = lambda:click('A'))
b2 = Button(win, text="B", command = lambda:click('B'))
b3 = Button(win, text="C", command = lambda:click('C'))
b4 = Button(win, text="D", command = lambda:click('D'))
b5 = Button(win, text="E", command = lambda:click('E'))
b6 = Button(win, text="F", command = lambda:click('F'))
b7 = Button(win, text="G", command = lambda:click('G'))
b8 = Button(win, text="H", command = lambda:click('H'))
b9 = Button(win, text="I", command = lambda:click('I'))
b10 = Button(win, text="J", command = lambda:click('J'))
b11 = Button(win, text="K", command = lambda:click('K'))
b12 = Button(win, text="L", command = lambda:click('L'))
b13 = Button(win, text="M", command = lambda:click('M'))
b14 = Button(win, text="N", command = lambda:click('N'))
b15 = Button(win, text="O", command = lambda:click('O'))
b16 = Button(win, text="P", command = lambda:click('P'))
b17 = Button(win, text="Q", command = lambda:click('Q'))
b18 = Button(win, text="R", command = lambda:click('R'))
b19 = Button(win, text="S", command = lambda:click('S'))
b20 = Button(win, text="T", command = lambda:click('T'))
b21 = Button(win, text="U", command = lambda:click('U'))
b22 = Button(win, text="V", command = lambda:click('V'))
b23 = Button(win, text="W", command = lambda:click('W'))
b24 = Button(win, text="X", command = lambda:click('X'))
b25 = Button(win, text="Y", command = lambda:click('Y'))
b26 = Button(win, text="Z", command = lambda:click('Z'))
b_hint = Button(win, text="Check hint", bg="orange", padx=20, pady=10, command=hint)



b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)
b4.grid(row=1, column=3)
b5.grid(row=1, column=4)
b6.grid(row=1, column=5)
b7.grid(row=1, column=6)
b8.grid(row=2, column=0)
b9.grid(row=2, column=1)
b10.grid(row=2, column=2)
b11.grid(row=2, column=3)
b12.grid(row=2, column=4)
b13.grid(row=2, column=5)
b14.grid(row=2, column=6)
b15.grid(row=3, column=0)
b16.grid(row=3, column=1)
b17.grid(row=3, column=2)
b18.grid(row=3, column=3)
b19.grid(row=3, column=4)
b20.grid(row=3, column=5)
b21.grid(row=3, column=6)
b22.grid(row=4, column=0)
b23.grid(row=4, column=1)
b24.grid(row=4, column=2)
b25.grid(row=4, column=3)
b26.grid(row=4, column=4)
b_hint.grid(row=5, column=1)


win.mainloop()