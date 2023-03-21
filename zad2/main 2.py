# a

a = b = c = 420
print(a == b)
print(b == c)
# b
print(type(a), type(b), type(c))
print(hex(id(a)), hex(id(b)), hex(id(c)))

# c
c = "Java 11"
# ac
print(a == b)
print(b == c)
# bc
print(type(a), type(b), type(c))
print(hex(id(a)), hex(id(b)), hex(id(c)))




def zly_znak(znak):
    if (znak == "*"):
        return 0
    elif znak == "/":
        return 0
    elif znak == "+":
        return 0
    elif znak == "-":
        return 0
    elif znak == "**":
        return 0
    elif znak == "-**":
        return 0
    else:
        return 1

def obliczenie (znak, x,y):
    if (znak == "*"):
        return x*y
    elif znak == "/":
        return x/y
    elif znak == "+":
        return x+y
    elif znak == "-":
        return x-y
    elif znak == "**":
        return pow(x,y)
    elif znak == "-**":
        return pow(x,-y)


def odpow(odp):
    if odp==1:
        return 0
    elif odp==2:
        return 0
    elif odp==3:
        return 0
    else: return 1

if __name__ == '__main__':
    x = int(input("podaj pierwsza zmienna"))
    y = int(input("podaj druga zmienna"))
    znak = input("podaj dzialanie ktore checsz przeprowadzic")
    while zly_znak(znak):
        znak = input("podaj dzialanie ktore checsz przeprowadzic")
    odp = obliczenie(znak,x,y)
    print(odp)
    odpowiedzi=[]
    print("------------")
    listaOdp1=["nic","sport","spanie"]
    print("Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:")
    print("1 nic")
    print("2 sport")
    print("3 ani 1, ani 2")
    odp1 = int(input("podaj swoja odp [1,2,3]"))
    while odpow(odp1):
        odp1 = int(input("podaj swoja odp [1,2,3]"))
    print(listaOdp1[odp1-1])
    odpowiedzi.insert(0,listaOdp1[odp1-1])

    print("------------")
    listaOdp1 = ["nie czytam", "podroza", "wolny czas"]
    print("W jakich okolicznościach czytasz książki najczęściej? ")
    print("1 nie czytam")
    print("2 podroza")
    print("3 wolny czas")
    odp1 = int(input("podaj swoja odp [1,2,3]"))
    while odpow(odp1):
        odp1 = int(input("podaj swoja odp [1,2,3]"))
    odpowiedzi.insert(1,listaOdp1[odp1 - 1])

    print("------------")
    listaOdp1 = ["0", "1", "2"]
    print("Ile książek czytasz średnio w ciągu roku? ")
    print("1 0")
    print("2 1")
    print("3 2")
    odp1 = int(input("podaj swoja odp [1,2,3]"))
    while odpow(odp1):
        odp1 = int(input("podaj swoja odp [1,2,3]"))
    odpowiedzi.insert(2,listaOdp1[odp1 - 1])


    print("--twoje odpowiedzi--\n\n\n")

    for i in odpowiedzi:
        print(i)
