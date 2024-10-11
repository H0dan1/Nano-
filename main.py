
import traceback, collections

def standaardprijs(afstandKM):
    if afstandKM <= 0:
        afstandKM = 0
    if  afstandKM >= 50:
        prijs = 15 + (0.60 * afstandKM)
    else:
        prijs = (0.80 * afstandKM)
    return

def ritprijs(leeftijd, weekendrit, afstandKM):


        prijs = standaardprijs(afstandKM)

        if leeftijd < 12 or leeftijd >= 65:
            if weekendrit:
                korting = 0.35
            else:
                korting = 0.30
        else:
            if weekendrit:
                korting = 0.40
            else:
                korting = 0.0

        prijs_met_korting = prijs * (1 - korting)

        return prijs_met_korting


def development_code():
    # Plaats hieronder code om je functies tussentijds te testen. Bijv:
    print("development printout:", standaardprijs(30))
    print("development printout: ",ritprijs(70 , True, 60))

def module_runner():
    development_code()      # Comment deze regel om je 'development_code' uit te schakelen


import traceback, collections

"""
Programming
Opdracht PROG: NS-Functies
(c) 2024 Hogeschool Utrecht,
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.
"""


def standaardprijs(afstandKM):
    """
    Bepaal de prijs van een treinrit. Iedere treinrit kost 80 cent per kilometer,
    maar als de rit langer is dan 50 kilometer betaal je een vast bedrag van €15,-
    plus 60 cent per kilometer.

    Ga bij invoer van negatieve afstanden uit van een afstand van
    0 kilometer (prijs is dan dus 0 Euro).

    Args:
        afstandKM (int): De reisafstand in kilometers.
    Returns:
        float: De berekende standaardprijs.
    """
    if afstandKM < 0:
        afstandKM = 0
    if afstandKM > 50:
        prijs = 15 + (0.60 * afstandKM)
    else:
        prijs = 0.80 * afstandKM
    return prijs


def ritprijs(leeftijd, weekendrit, afstandKM):
    """
    Het eerste wat deze functie moet doen, is het aanroepen van
    functie standaardprijs, waarbij de afstand in kilometers doorgegeven
    moet worden om de standaardprijs voor de rit op te vragen.

    Aan de hand van de standaardprijs kan de actuele ritprijs worden berekend.
    De regels zijn als volgt:

     * Op werkdagen reizen kinderen (onder 12 jaar) en ouderen (65 en ouder) met 30% korting.
     * In het weekend reist deze groep met 35% korting.
     * Overige leeftijdsgroepen betalen de gewone prijs, behalve in het weekend. Dan reist
       deze leeftijdsgroep met 40% korting.

    Args:
        leeftijd (int): De leeftijd van de reiziger in gehele jaren.
        weekendrit (bool): True als het een rit in het weekend betreft, anders False.
        afstandKM (int): De reisafstand in kilometers.
    Returns:
        float: De berekende ritprijs.
    """
    # Haal de standaardprijs op
    prijs = standaardprijs(afstandKM)

    # Bepaal de kortingspercentage
    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit:
            korting = 0.35  # 35% korting in het weekend
        else:
            korting = 0.30  # 30% korting op werkdagen
    else:
        if weekendrit:
            korting = 0.40  # 40% korting in het weekend
        else:
            korting = 0.0  # Geen korting op werkdagen

    # Bereken de uiteindelijke prijs na korting
    prijs_met_korting = prijs * (1 - korting)

    return prijs_met_korting


def development_code():
    # Plaats hieronder code om je functies tussentijds te testen. Bijv:
    print("development printout:", standaardprijs(30))
    print("development printout:", ritprijs(70, True, 60))


def module_runner():
    development_code()  # Comment deze regel om je 'development_code' uit te schakelen


# Functie standaardprijs berekent de standaardprijs voor de rit op basis van afstand
def standaardprijs(afstandKM):
    if afstandKM < 0:
        afstandKM = 0
    if afstandKM > 50:
        prijs = 15 + (0.60 * afstandKM)
    else:
        prijs = 0.80 * afstandKM
    return prijs















def ritprijs(leeftijd, weekendrit, afstandKM):

    prijs = standaardprijs(afstandKM)


    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit:
            korting = 0.35
        else:
            korting = 0.30
    else:
        if weekendrit:
            korting = 0.40
        else:
            korting = 0.0


    prijs_met_korting = prijs * (1 - korting)

    return prijs_met_korting


# Voorbeeld van gebruik
afstand = 45  # 60 km rit
leeftijd = 12  # Oudere persoon
weekendrit = True  # Rit in het weekend

print(f"De ritprijs is: €{ritprijs(leeftijd, weekendrit, afstand):.2f}")


