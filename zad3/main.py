import random
import getpass
import webbrowser;
def _min(tab):
    min= tab[0]
    for x in range(1,len(tab)):
        if(tab[x]<min):
            min=tab[x]
    return min

def _max(tab):
    max= tab[0]
    for x in range(1,len(tab)):
        if(tab[x]>max):
            max=tab[x]
    return max

def _wycieczka():
    miasta=["Warszawa", "Kraków","Szczecin","Łódź","Wroclaw","Zielona Góra","Gdańsk",
            "Poznań","Świnoujście","Dąbrowa Górnicza"]
    uzyteMiasta=[]
    while len(uzyteMiasta) != len(miasta):
        rancd=random.randint(0,9)
        if  not any(x in miasta[rancd] for x in uzyteMiasta):
            uzyteMiasta.append(miasta[rancd])
    for x in range (0,len(uzyteMiasta)):
        print(uzyteMiasta[x])


def _walka(g1,g2):
    if g1==1:
        if g2==1: return 0
        if g2==2: return -1
        if g2==3: return 1
    elif g1==2:
        if g2==1: return 1
        if g2==2: return 0
        if g2==3: return -1
    elif g1 == 1:
        if g2 == 1: return -1
        if g2 == 2: return 1
        if g2 == 3: return 0

def znaki(znak):
    if znak==1: return "kamien"
    elif znak==2: return "papier"
    elif znak==3: return "nozyce"
def _Papier_Kamien_Nozyce():
    wyborG1=0
    wygrane1=0
    wygrane2=0
    linia=input("grasz na komputer [k]/ na innego gracza [g]")
    while(linia!="k" and linia!="g"):

        linia = input("grasz na komputer [k]/ na innego gracza [g]")

    koniecGry=False
    while(not koniecGry):
        print("--Ruch gracza--")
        wyborG=int(getpass.getpass("| [1] - kamien | [2] - papier | [3] - nozyce |"))
        while wyborG!=1 and wyborG!=1 and wyborG!=3:
            wyborG = getpass.getpass("| [1] - kamien | [2] - papier | [3] - nozyce |")

        if linia == "g":
            print("ruch gracza 2")
            input("press any key to continue")
            wyborG1 = int(getpass.getpass("| [1] - kamien | [2] - papier | [3] - nozyce |"))
            while wyborG1 != 1 and wyborG1 != 2 and wyborG1 != 3:
                wyborG1 = getpass.getpass("| [1] - kamien | [2] - papier | [3] - nozyce |")
        else: wyborG1=random.randint(1,3)


        print("walka")
        print("gracz 1 wybrał ",znaki(wyborG), "gracz 2 wybrał ", znaki(wyborG1))

        rezultat = _walka(wyborG,wyborG1)
        if rezultat==1:
            wygrane1+=1
            print("wygrywa gracz 1")
        elif rezultat==-1:
            wygrane2 += 1
            print("wygrywa gracz 2")
        elif rezultat == 0:
            print("remis")
        grac=input("grac dalej? [t/n]")

        while grac!="t" and grac !="n":
            grac = input("grac dalej? [t/n]")
        if grac=="n": koniecGry=True
    print("ostateczny wynik to ",wygrane1, "do", wygrane2)

if __name__ == '__main__':
    # linia = input("podaj liczby po przecinku")
    # znaki = linia.split(",")
    # print("min ",_min(znaki))
    # print("max ",_max(znaki))
    # _wycieczka()
    _Papier_Kamien_Nozyce()