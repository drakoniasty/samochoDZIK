from tkinter import *






def nastepna_karoseria():
    global numer_karoserii
    
    global karoseria
    
    numer_karoserii+=1
    
    plotno_tlo.delete(karoseria)
    
    if numer_karoserii > 2:
        numer_karoserii=0
    
    karoseria=plotno_tlo.create_image(10,100,anchor=NW,image=karoseria_auta[numer_karoserii])
    
    plotno_tlo.pack()
    
def poprzednia_karoseria():
    global numer_karoserii
    
    global karoseria
    
    numer_karoserii-=1
    
    plotno_tlo.delete(karoseria)
    
    if numer_karoserii<0:
        numer_karoserii=2
    
    karoseria=plotno_tlo.create_image(10,100,anchor=NW,image=karoseria_auta[numer_karoserii])
    plotno_tlo.pack()

def nastepna_maska():
    global numer_maski
    
    global maska
    
    numer_maski+=1
    
    plotno_tlo.delete(maska)
    
    if numer_maski > 2:
        numer_maski=0
    
    maska=plotno_tlo.create_image(281,170,anchor=NW,image=maski_auta[numer_maski])
    
    plotno_tlo.pack()
    
def poprzednia_maska():
    global numer_maski
    
    global maska
    
    numer_maski-=1
    
    plotno_tlo.delete(maska)
    
    if numer_maski < 0:
        numer_maski=2
    
    maska=plotno_tlo.create_image(281,170,anchor=NW,image=maski_auta[numer_maski])
    
    plotno_tlo.pack()
    
    
def nastepne_kola():
    global numer_kola
    
    global kola
    
    numer_kola+=1
    
    plotno_tlo.delete(kola)
    
    if numer_kola > 2:
        numer_kola=0
    
    kola=plotno_tlo.create_image(75,220,anchor=NW,image=kola_auta[numer_kola]),plotno_tlo.create_image(318,220,anchor=NW,image=kola_auta[numer_kola])
    
    plotno_tlo.pack()
    
def poprzednie_kola():
    global numer_kola
    
    global kola
    
    numer_kola-=1
    
    plotno_tlo.delete(kola)
    
    if numer_kola < 0:
        numer_kola=2
    
    kola=plotno_tlo.create_image(75,220,anchor=NW,image=kola_auta[numer_kola]),plotno_tlo.create_image(318,220,anchor=NW,image=kola_auta[numer_kola])
    
    plotno_tlo.pack()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def inne_tlo_przod():
    
    
    global numer_karoserii
    global karoseria

    global numer_maski
    global maska
    
    global numer_kola
    global kola
    
    global tlo
    global numer_tla
    
    
    
    
    
    
    
    
    
    
    
    
    numer_tla+=1
    
    plotno_tlo.delete(tlo)
    plotno_tlo.delete(maska)
    plotno_tlo.delete(kola)
    plotno_tlo.delete(karoseria)
    
    
    
    
    
    
    
    if numer_tla>2:
        numer_tla=0
    

    
    tlo=plotno_tlo.create_image(0,200,anchor=NW,image=tla[numer_tla])
    
    karoseria=plotno_tlo.create_image(10,100,anchor=NW,image=karoseria_auta[numer_karoserii])
    
    maska=plotno_tlo.create_image(281,170,anchor=NW,image=maski_auta[numer_maski])
    
    kola=plotno_tlo.create_image(75,220,anchor=NW,image=kola_auta[numer_kola]),plotno_tlo.create_image(318,220,anchor=NW,image=kola_auta[numer_kola])
    
    plotno_tlo.pack()    
 
 
 
 
 
 
 
 
 
def inne_tlo_tyl():
    
    
    global numer_karoserii
    global karoseria
    global numer_maski
    global maska
    global numer_kola
    global kola
    
    global tlo
    global numer_tla
    
    numer_tla-=1
    
    plotno_tlo.delete(tlo)
    plotno_tlo.delete(maska)
    plotno_tlo.delete(kola)
    plotno_tlo.delete(karoseria)
    
    if numer_tla < 0:
        numer_tla=2
    
    tlo=plotno_tlo.create_image(0,200,anchor=NW,image=tla[numer_tla])
    karoseria=plotno_tlo.create_image(10,100,anchor=NW,image=karoseria_auta[numer_karoserii])
    maska=plotno_tlo.create_image(281,170,anchor=NW,image=maski_auta[numer_maski])
    kola=plotno_tlo.create_image(75,220,anchor=NW,image=kola_auta[numer_kola]),plotno_tlo.create_image(318,220,anchor=NW,image=kola_auta[numer_kola])
    plotno_tlo.pack()        






moje_okno = Tk()
moje_okno.title("gierka")
moje_okno.geometry("800x800")


moje_okno.configure(background="aquamarine",cursor="pirate")








przod1 = PhotoImage(file="przod1.png")
przod2 = PhotoImage(file="przod2.png")
przod3 = PhotoImage(file="przod3.png")

karo1 = PhotoImage(file="karo1.png")
karo2 = PhotoImage(file="karo2.png")
karo3 = PhotoImage(file="karo3.png")

kolo1 = PhotoImage(file="kolo1.png")
kolo2 = PhotoImage(file="kolo2.png")
kolo3 = PhotoImage(file="kolo3.png")






tlo1 = PhotoImage(file="road.png")
tlo2 = PhotoImage(file="road2.png")
tlo3 = PhotoImage(file="road3.png")






















numer_karoserii=0
numer_maski=0
numer_kola=0

numer_tla=0








maski_auta=[przod1,przod2,przod3]

karoseria_auta=[karo1,karo2,karo3]

kola_auta=[kolo1,kolo2,kolo3]


tla=[tlo1,tlo2,tlo3]




tekst = Label(text="Lubie SAMOCHODY")


tekst.configure(bg="red",fg="yellow",font=("",12), bd=20,relief=SUNKEN,cursor="spider")

#tekst.place(x=100,y=150)
tekst.pack(fill=X,side=TOP)




plotno_tlo=Canvas(moje_okno,height=400,width=500, background="pink", highlightbackground="red", cursor="target")





tlo=plotno_tlo.create_image(0,200,anchor=NW,image=tla[numer_tla])

maska=plotno_tlo.create_image(281,170,anchor=NW,image=maski_auta[numer_maski])

karoseria=plotno_tlo.create_image(10,100,anchor=NW,image=karoseria_auta[numer_karoserii])

kola=plotno_tlo.create_image(75,220,anchor=NW,image=kola_auta[numer_kola]),plotno_tlo.create_image(318,220,anchor=NW,image=kola_auta[numer_kola])



plotno_tlo.pack(side=TOP)
#plotno_tlo.place(x=10,y=20)



autor = Label(text="Konrad Wieczorek")
autor.configure(bg="aqua",fg="magenta",font=("Arial",15,"underline"),cursor="sizing")
autor.pack(side=BOTTOM)


przycisk_przod_karoseria=Button(moje_okno,text="Wybierz poprzedni kolor karoserii", font=("Calibri",15,"bold"),width=30, bg="red",fg="purple",activebackground="pink",command=poprzednia_karoseria, cursor="exchange")
przycisk_przod_karoseria.place(x=50,y=480)

przycisk_wstecz_karoseria=Button(moje_okno,text="Wybierz następny kolor karoserii",width=30, bg="red",fg="purple", font=("Calibri",15,"bold"), command=nastepna_karoseria, cursor="plus")
przycisk_wstecz_karoseria.place(x=400,y=480)

przycisk_przod_karoseria=Button(moje_okno,text="Wybierz poprzedni kolor maski", font=("Calibri",15,"bold"),width=30, bg="red",fg="purple",activebackground="pink",command=poprzednia_maska, cursor="exchange")
przycisk_przod_karoseria.place(x=50,y=550)

przycisk_wstecz_karoseria=Button(moje_okno,text="Wybierz następny kolor maski",width=30, bg="red",fg="purple", font=("Calibri",15,"bold"), command=nastepna_maska, cursor="plus")
przycisk_wstecz_karoseria.place(x=400,y=550)

przycisk_przod_karoseria=Button(moje_okno,text="Wybierz poprzedni kolor kół", font=("Calibri",15,"bold"),width=30, bg="red",fg="purple",activebackground="pink",command=poprzednie_kola, cursor="exchange")
przycisk_przod_karoseria.place(x=50,y=620)

przycisk_wstecz_karoseria=Button(moje_okno,text="Wybierz następny kolor kół",width=30, bg="red",fg="purple", font=("Calibri",15,"bold"), command=nastepne_kola, cursor="plus")
przycisk_wstecz_karoseria.place(x=400,y=620)








przycisk_zmien_tlo_przod=Button(moje_okno,text="Zmień na kolejne tło", font=("Calibri",15,"bold"),width=30, bg="red",fg="purple",activebackground="pink",command=inne_tlo_przod, cursor="exchange")

przycisk_zmien_tlo_przod.place(x=50,y=690)

przycisk_zmien_tlo_wstecz=Button(moje_okno,text="Zmień na poprzednie tło", font=("Calibri",15,"bold"),width=30, bg="red",fg="purple",activebackground="pink",command=inne_tlo_tyl, cursor="exchange")
przycisk_zmien_tlo_wstecz.place(x=400,y=690)




