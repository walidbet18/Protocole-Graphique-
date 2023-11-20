import matplotlib.pyplot as plt



# fonction qui converte le message a un tableau des bits
def convertToBit(msg):
    tab = []
    for i in msg:
        asci = ord(i)
        t = []

        if (asci == 0):
            tab.extend(0)

        while asci > 0:
            q = asci // 2
            r = asci % 2
            t.append(r)
            asci = q

        t.reverse()
        tab.extend(t)

    return tab


# fonction qui genere le code hamming
def codeHamming(tab):
    l = ""
    for i in tab:
        l += str(i)

    liste = list(l)
    liste.reverse()
    tab1 = []
    a = 0
    b = 0
    c = 0
    d = 0

    while (len(liste) + d + 1 > 2 ** d):
        d = d + 1

    for i in range(0, (d + len(liste))):
        p = 2 ** a

        if (p == (i + 1)):
            a = a + 1
            tab1.append(0)

        else:
            k = int(liste[c])
            tab1.append(k)
            c = c + 1

    for p in range(0, (len(tab1))):
        e = 2 ** b
        if (e == (p + 1)):
            si = e - 1
            j = si
            tab2 = []

            while (j < len(tab1)):
                pl = tab1[j:j + e]
                tab2.extend(pl)
                j = j + 2 * e

            for i in range(1, len(tab2)):
                tab1[si] = tab1[si] ^ tab2[i]
            b = b + 1

    tab1.reverse()

    return tab1




def codage(tab):
    p = 0.2
    X = 0
    Y = 0
    j = 1

    figure, ax = plt.subplots()
    cercle = plt.Circle((X, Y), p, fill=False, color='red')  #le cercle de depart
    ax.add_artist(cercle)
    cercle = plt.Circle((X, Y), p + j * 0.1, fill=False, color='red')  #le cercle de décalage
    ax.add_artist(cercle)
    j = 2

    for i in tab:
        if (i > 0):
            cercle = plt.Circle((X, Y), p + j * 0.1, fill=False)
            ax.add_artist(cercle)
        j = j + 1

    plt.xlim(-0.5 - 0.1 * j, 0.5 + j * 0.1)
    plt.ylim(-0.5 - 0.1 * j, 0.5 + j * 0.1)
    ax.set_aspect(1)
    ax.add_artist(cercle)

    plt.show()


msg = input("Entrez le message: ")
tab = convertToBit(msg)
print("le message converti en bit:",tab)

h = codeHamming(tab)
print("Code Hamming : ", h)

# Foncrion qui trace le message
codage(h)

