from random_word import RandomWords
cuvants = RandomWords()
word = str(cuvants.get_random_word(maxLength=6))
cuvant_final = ""
linii = []
cuvant = []
viata = 5
litereF = []
Z = 0
def stickman():
    print("          _")
    print("         (_)")
    print("         _;")
    print("        / | \ ")
    print("        \ |  \ ")
    print("         `|\  ` ")
    print("          | \ ")
    print("         /  /")
    print("        /  /_")
    print("        ` ")
vieti = input("Alege dificultatea: 1.easy , 2.medium ,3.hard: ")
if vieti.lower() == "easy":
    viata = 10
elif vieti.lower() == "medium":
    viata = 5
elif vieti.lower() == "hard":
    viata == 3
else:
    print("Scrie cuvantul (ex:easy) !!!! ")
    exit()
stickman()
for i in range(len(word)): #pentru facut cate linii sunt
    linii.append("_")
for zzz in word:
    cuvant_final = cuvant_final + zzz
print("Cuvantul tau are "+str(len(linii))+" litere")
print(*linii)
while linii.count("_") > 0:  # daca nu mai sunt _ se incheie
    litera = input("Alege o litera: ")

    if len(litera) > 1:
        print("DOAR LITERE!!!")
        viata -= 1
        print("Mai ai "+str(viata)+" vieti")
        if viata < 1:
            for vieti in range(5):
                print("GAME OVER!!! <o/")
            exit()

    else:
        if litera in word:  # daca e vreun caracter executa
            for zxc in range(len(linii)):   # de atatea ori
                if word.find(litera , zxc) >= 0:
                    c = word.find(litera, zxc)  # gaseste un caracter
                    linii[c] = litera
        else:
            litereF.append(litera)
            print("Gresit!!!")
            viata -= 1
            print("Mai ai " + str(viata) + " incercari")
            if viata < 1:
                for vieti in range(5):
                    print("GAME OVER!!! <o/")
                print("\n \n Cuvantul era: " + word)
                exit()
        print("Litere folosite care nu au mers: "+str(litereF))

    print(*linii)
print("bravo , cuvantul era \""+cuvant_final+"\" ai reusit")
