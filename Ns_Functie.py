#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback, collections
from pprint import PrettyPrinter

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
    # Als de afstand negatief is gaat het terug naar 0
    if afstandKM < 0:
        afstandKM = 0

    # in het volgende stuk word de afstand berekent aan de hand van of het meer of minder dan 50 km is
    if afstandKM > 50:
        prijs = 15 + (0.60 * afstandKM)
    else:
        prijs = 0.80 * afstandKM #
    return prijs # Hier vraag ik de functie om de prijs terug te geven


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
    prijs = standaardprijs(afstandKM) # standaardprijs word berekent door midel van de afstand in km.

    if leeftijd < 12 or leeftijd >= 65: #controleert of de persoon jonger is dan 12 of ouder is dan 65.
        if weekendrit:
            korting = 0.35 # 35% korting in het weekend.
        else:
            korting = 0.30 # 30% korting door de weeks.
    else:
        if weekendrit: # voor reizigers tussen 12 en 65 die de weekend rit nemen.
            korting = 0.40 # 40% korting in het weekend.
        else:
            korting = 0.0 # geen korting geldig buiten de weekend

    prijs_met_korting = prijs * (1 - korting)
    return prijs_met_korting # de functie geeft de prijs terug met korting erbij


def development_code():
    # Plaats hieronder code om je functies tussentijds te testen. Bijv:
    print("development printout:", standaardprijs(30))


print ('Hallo en welkom bij NS "Help bereken mijn rit" service!: ')

print("Ik zal u helpen bij het berekenen van u ritprijs en laten zien hoeveel u reis gaat kosten. ")

print()
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

    prijs_met_korting = prijs * (1 - korting) # De korting op de standaardprijs word afgetroken

    return prijs_met_korting

print("Laten we je reis samen plannen!")
aantal_ritten = int(input("Hoeveel ritten wilt u berekenen? ")) # Zodra de gebruiker de aantal ritten hier invoert zal de onderste loop gebruikt worden.

for i in range(aantal_ritten): # Met deze functie heb ik een loop kunnen instellen dat aantal x  ritten die de gebruiker invult blijft herhalen.
    print(f"\nRit plan {i + 1}:")
    leeftijd = int(input("Voer u leeftijd in: "))
    afstand = float(input("Voer de afstand die u reist in kilometers in: "))
    weekend_input = input("Gaat u in het weekend reizen? (ja/nee): ").lower()
    weekendrit = True if weekend_input == "ja" else False


    prijs = ritprijs (leeftijd, weekendrit, afstand)
    print(f"De ritprijs is: €{prijs:.2f}\n\n") # Dankzij de f string is het mogelijk om een cijfer  te krijgen met twee decimalen.

    print("Dit is de einde van de service 'Help bereken mijn rit'! ")
    print("Ik wens u een fijne reis")

    print()

    print()

def module_runner():
    development_code()      # Comment deze regel om je 'development_code' uit te schakelen
    __run_tests()           # Comment deze regel om de HU-tests uit te schakelen



"""
==========================[ HU TESTRAAMWERK ]================================
Hieronder staan de tests voor je code -- daaraan mag je niets wijzigen!
"""


def __my_assert_args(function, args, expected_output, check_type=False):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.
    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output).__name__} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    if str(expected_output) == str(output):
        msg = f"Fout: {function.__name__}{argstr} geeft {output} ({type(output).__name__}) " \
              f"in plaats van {expected_output} (type {type(expected_output).__name__})"
    else:
        msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"

    if type(expected_output) is float and isinstance(output, (int, float, complex)):
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_standaardprijs():
    case = collections.namedtuple('case', 'distance expected_output')

    testcases = [ case(-51, 0), case(-10, 0), case(0, 0), case(10,8),
                  case(49, 39.2), case(50, 40), case(51, 45.6), case(80, 63) ]

    for test in testcases:
        __my_assert_args(standaardprijs, (test.distance,), test.expected_output)


def test_ritprijs():
    case = collections.namedtuple('case', 'age weekend distance expected_output')

    testcases = [ case(11, True,  50, 26.0),  case(11, False,  50, 28.0), case(11, True,  51, 29.64),
                  case(11, False, 51, 31.92), case(11, True, -51,  0.0),  case(11, False, -51,  0.0),
                  case(12, True,  50, 24.0),  case(12, False, 50, 40.0),  case(12, True,  51, 27.36),
                  case(12, False, 51, 45.6),  case(12, True, -51,  0.0),  case(12, False, -51, 0.0),
                  case(64, True,  50, 24.0),  case(64, False,  50, 40.0), case(64, True,  51, 27.36),
                  case(64, False, 51, 45.6),  case(64, True, -51,  0.0),  case(64, False, -51,  0.0),
                  case(65, True,  50, 26.0),  case(65, False, 50, 28.0),  case(65, True,  51, 29.64),
                  case(65, False, 51, 31.92) ]

    for test in testcases:
        __my_assert_args(ritprijs, (test.age, test.weekend, test.distance), test.expected_output)


def __run_tests():
    """ Test alle functies. """
    tes






























