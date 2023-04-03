# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
from tokenize import String


def obliczanie(podX, podY, kafX, kafY, iloswOP):
    wielkoscPod= podX * podY+0.1*podX * podY
    wielkscKaf= kafX*kafY
    kafelkiWop=wielkscKaf*iloswOP
    print(wielkoscPod/kafelkiWop)
    return math.ceil(wielkoscPod/kafelkiWop)

def pierwsze():
    lista=[3,4,5,6,7,8,9,10,11,12,13]
    wynik = []

    for x in lista:
        variable : bool = True
        if x>1:
            for i in range(2, int(math.sqrt(x)+1),1):
                if x%i==0:
                    variable=False
                    break

            if variable:
                wynik.append(x)
                print(wynik)

    return lista


def Cezar(tekst, klucz):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    if klucz> len(alphabet):
        wielokrot=int(klucz/len(alphabet))-1
        klucz=len(alphabet)*wielokrot
    wynik=""
    tekst=tekst.lower()
    for i in  range(len(tekst)):
        for w in  range(len(alphabet)):
            if alphabet[w] == tekst[i]:
                index=w+klucz
                if index>len(alphabet):
                    index=index-len(alphabet)
                wynik+=alphabet[index]

    print(wynik)


if __name__ == '__main__':
    #
    # podx= float(input("podaj x podlogi"))
    # pody = float(input("podaj y podlogi"))
    # kafx = float(input("podaj x kafelka"))
    # kafy = float(input("podaj y kafelka"))
    # iloscWOp = float(input("podaj ilosc w kaf"))
    # print(obliczanie(podx,pody,kafx,kafy,iloscWOp))

    pierwsze()
    Cezar("abcd123", 1)