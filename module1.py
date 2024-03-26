from tkinter import *
import string
import random
from time import sleep

def registreerimine(kasutajad:list,paroolid:list)->any:
    """Funktsioon tagastab 2 listid
    :param list kasutaja: Kasutaja nimede kirjeldus
    :param list paroolid: Kasutaja nimed paroolid
    :rtype: list,list
    """
    while True:
        nimi=input("Mis on sinu nimi on? ")
        if nimi not in kasutajad:
            while True:
                parool=input("Mis on sinu parool? ")
                flag_p=False
                flag_l=False
                flag_u=False
                flag_d=False
                if len(parool)>=8:
                    parool_list=list(parool)
                    for p in parool_list:
                        if p in string.punctuation:
                            flag_p=True
                        elif p in string.ascii_lowercase:
                            flag_l=True
                        elif p in string.ascii_uppercase:
                            flag_u=True
                        elif p in string.digits:
                            flag_d=True
                    if flag_p and flag_u and flag_l and flag_d:
                        kasutajad.append(nimi)
                        paroolid.append(parool)
                        break
                    else:
                        print("Nõrk salasõna!")
                else:
                    print("Nõrk salasõna! Parool peab olema vähemalt 8 tähemärki pikk.")
            break
        else:
            print("Selline kasutaja on juba olemas!")
    return kasutajad, paroolid

def autoriseerimine(kasutajad:list,paroolid:list):
    """Funktsioon kuvab ekraanile "Tere tulemas! kui kasutaja on olemas nimekirjas
    Nimi on järjendis kasutajad
    Salasõna on paroolide järjendis
    Nimi ja salasõna indeksid on võrdsed
    :param list kasutajad: Kasutaja nimede kirjeldus
    :param list paroolid: Kasutaja nimed paroolid
    """
    p=0
    while True:
        nimi=input("Sisesta kasutajanimi: ")
        if nimi in kasutajad:
            parool=input("Sisesta salasõna: ")
            while True:
                p+=1
                try:
                    if kasutajad.index(nimi)==paroolid.index(parool):
                       print(f"Tere tulemast! {nimi}")
                       break
                except:
                    print("Vale nimi või salasõna!")
                    if p==5:
                        print("Proovi uuesti 10 sekundi pärast")
                        for i in range(10):
                            sleep(1)
                            print(f"On jäänud {10-i} sekundit")
        else:
             print("Kasutajat pole")

def nimi_või_parooli_muurmine(list_:list):
    """
    """
    muutuja=input("Vana nimi või parool: ")
    if muutuja in list_:
        indeks=list_.index(muutuja)
        muutuja=input("Uus nimi või parool: ")
        list_[indeks]=muutuja
    return list_

def genereerida_parooli(length:int)-> str:
    """Funktsioon loob parooli
    Looge etteantud pikkusega parool.
    """
    result=[]
    choices=string.ascii_letters+string.digits
    while len(result)<length:
         symbol=random.choice(string.ascii_letters+string.digits)
         result.append(symbol)
    return "".join(result)

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

def register_user(kasutajad, paroolid):  # Добавляем параметры kasutajad и paroolid
    username = username_entry.get()
    password = password_entry.get()

    # Регистрация пользователя
    result = registreerimine(kasutajad, paroolid)
    kasutajad, paroolid = result

def login_user():
    username = username_entry.get()
    password = password_entry.get()

    # Аутентификация пользователя
    autoriseerimine(kasutajad, paroolid)

# Генерация начальных пользователей и паролей
kasutajad = []
paroolid = []

aken=Tk()
aken.geometry("800x500")
aken.title("Akna pealkiri")
aken.configure(bg="#000000")
# aken.iconbitmap("icon.ico")
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
# pilt=PhotoImage(file="scary.png")
var=BooleanVar() #Intvar(),Stringvar()
valik=Checkbutton(raam,
                  # image=pilt,
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

# Добавляем виджеты для регистрации и аутентификации
register_button = Button(aken, text="Registreeri", command=lambda: register_user(kasutajad, paroolid))
login_button = Button(aken, text="Logi sisse", command=login_user)
username_label = Label(aken, text="Kasutajanimi:")
password_label = Label(aken, text="Parool:")
username_entry = Entry(aken)
password_entry = Entry(aken, show="*")
