
from tkinter import *

def tehtudvalik(var):
    f=var.get()
    if f:
        texbox.configure(show="")
    else:
        texbox.configure(show="*")
def textpealkijasse():
    t=texbox.get()
    pealkiri.configure(text=t)
    texbox.delete(0,END)
aken=Tk()
aken.geometry("800x500")
aken.title("Akna pealkiri")
aken.configure(bg="#000000")
aken.iconbitmap("icon.ico")
pealkiri=Label(aken,
               text="Põhielemendid",
               bg="#141414",
               fg="#f5f0f2",
               cursor="spider",
               font="Impact 16",
               justify=CENTER,
               height=3,
               width=26)
raam=Frame(aken)
texbox=Entry(raam,
             bg="#f5f0f2",
             fg="#141414",
             font="Impact 16"
             ,width=26,
             show="*")
pilt=PhotoImage(file="scary.png")
var=BooleanVar() #Intvar(),Stringvar()
valik=Checkbutton(raam,
                  image=pilt,
                  variable=var,
                  onvalue=True,
                  offvalue=False,
                  command=lambda: tehtudvalik(var))
valik.deselect()
nupp=Button(raam,
            text="Vajuta mind",
            bg="#f5f0f2",
            fg="#141414",
            width=16,
            font="Impact 16",
            command=textpealkijasse)

pealkiri.pack()
raam.pack()
texbox.grid(row=0,column=0)
valik.grid(row=0,column=1)
nupp.grid(row=0,column=2)
aken.mainloop()

aken.mainloop()
