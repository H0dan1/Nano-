

print(5)
print(type(5))
print(5.0)
print(type(5.0))
print(5%2)
print(type(5%2))
print(5>1)
print(type(5>1))
print("5")
print(type("5"))
print(5*2)
print(type(5*2))


print()
print()
print()
print()
print()
print()



len('Supercalifragilisticexpialidocious')
print(len('Supercalifragilisticexpialidocious'))

len('Hodan')
print(len('Hodan'))
len('123456789')
print(len('123456789'))

print('o' in 'hodan')


print()
print()
print()

print('ice' in 'Supercalifragilisticexpialidocious')

print("Hello world")

print(len("Fartuun") > len("Hodan"))

print(sorted(['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'])[0])

print(sorted(["hodan","Bashir"])[0])
print()
print()
print()
print()

print(len("Supercalifragilisticexpialidocious"))

print("ice" in "Supercalifragilisticexpialidocious")

print(len("Antidisestablishmentarianism") > len("Honorificabilitudinitatibus"))

print(sorted(["Berlioz", "Borodin", "Brian", "Bartok", "Bellini", "Buxtehude", "Bernstein"])[-1])



a = 6
b = 7
som = (a + b)
print(som)

c = ( som )
gemiddelde = (som) /2
print(c)

voornaam = "hodan"
achternaam = "Data"

mijnnaam = ("hodan" + " Data")
print(mijnnaam)

print("a", a)
print("b", b)
print("c", c)
print(mijnnaam)

print()
print()


voorwaarden1= 6.75 > a and 6.75 < b
print(voorwaarden1)
voorwaarden2= len(mijnnaam) == (len(voornaam) + len(achternaam))
print(voorwaarden2)
voorwaarden3= len(mijnnaam) >= 5 *c
print(voorwaarden3)


k = 7
m = 8

check = 7 < m and 8 > m
print(check)



print("einde zin ")




fav = ["weekend"]
fav.append("artic")
fav[1] = "bts"
print(fav)


print("hiiiiiii")
print()
print()



lst = [3,7,-2,12]
bereik =  max(lst) - min(lst)
print(bereik)

lst = [4,9,-33,8]
bereik = max(lst) + min(lst)
print(bereik)


print()
print()

letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')


a = letters.count("A")
b = letters.count("B")
c = letters.count("C")

Totaal = (a,b,c)
print(Totaal)



zin = ("ik ga tv kijken en daarna ga ik kijken of de tv verkoopbaar is en iemand een tv zoekt")
aantal_keer = zin.count ("tv")
print(aantal_keer)


getal = ("1", "2", "3", "3", "2", "3", "3","4", "5")
aantal_keer = getal.count ("3")
print(aantal_keer)
aantal_keer = getal.count ("2")
print(aantal_keer)
print()
print()

# 1
print(0 == (1 == 2))

# 2
print(2 + (3 == 4) + 5 == 7)

# 3
print((1 < -1) == (3 > 4))



#Geef je score: 18
#Gefeliciteerd!
# Met een score van 18 ben je geslaagd!





print()
print()
print()

#Maanden 3 t/m 5 (maart, april, mei) horen bij de lente.
#Maanden 6 t/m 8 (juni, juli, augustus) horen bij de zomer.
#Maanden 9 t/m 11 (september, oktober, november) horen bij de herfst.
#Maanden 12, 1 en 2 (december, januari, februari) horen bij de winter.
#Als de gebruiker een maandnummer invoert dat buiten het bereik van 1 t/m 12 valt, zoals 0 of 13, geeft het programma 'ongeldig' terug.



print("----------------------------------------------------------------------------------------------")






dagen = ["maandag", "Dinsdagen", "Woensdag"]


for dag in dagen:
    print(dag[ : 2])




fruiten = ['appel', 'banaan', 'kers', 'druif', 'mango']

for fruit in fruiten:
    print(fruit [:3])





getalen = ["1", "4", "8", "7", "5", "9", "3"]

for getal in getalen:
    getalen_int = int(getal)
    if getalen_int % 2 == 0 :
        print(getalen_int)









print("einde")



s = "Guido van Rossum heeft programmeertaal Python bedacht."
letters = "a","e", "i", "o", "u"

for character in s:
    if character in letters:
        print(character)

print("einde\n")

s = "Python is een krachtige programmeertaal voor moderne toepassingen."

alfa = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

for character in s:
    if character in alfa:
        print(character)

print("einde\n")

print("einde\n")


s = ("ik ben hodan en ik moet dit begrijpen")

letters = "aeit"

for character in s:
    if character in letters:
        print(character)





print("einde\n")
print("einde\n")


def som (getal1, getal2, getal3):
    return getal1 + getal2 + getal3
resultaat = som (5,10,15)
print("de som is: ", resultaat)



# def optellen (nummer1, nummer2, nummer3):
#      return nummer1 + nummer2 + nummer3
# einde = optellen (2, 4, 6 )
# print("de som van nummer is:", einde)

# def som (getallenLijst):
#     return sum (getallenLijst)
# einde = som ([1,2,3,4,5])
# print("de som van nummer is:", einde)


# def gemiddelde( ):
#     zin = input("voer een zin: ")
#     woorden = zin.split()
#     totaal_lengte =  sum(len(woord) for woord in woorden)
#     aantal_woorden = len(woorden)
#
#     if aantal_woorden == 0:
#             return 0
#
#     gemiddelde_lengte = totaal_lengte / aantal_woorden
#     return gemiddelde_lengte
#
# resultaat = gemiddelde()
# print("de gemdiddelde lengte is van de woorden is,", resultaat)


# for i  in  range (1,11):
#     for j in range (1,11):
#         bereken = i * j
#         print(f"{i} x {j} = {bereken}")


# teller = 0
# som = 0
#
# while True:
#     getal = int(input("geef een getal: "))
#
#     if getal == 0:
#         break
#     teller += 1
#     som += getal
#     print(f"er zijn {teller} getallen ingevoerd de som is: {getal}")


while True:
    antwoord = int(input("geef een string met 4 letters: "))
    aantal_charachaters = len(antwoord)
    if aantal_charachaters != 4:
        print(f"{antwoord} is niet {aantal_charachaters} letters")
        continue
    else:
        print(f"de antwoord van {antwoord} is correct! ")
    break

ord("g")\
    pr
















