#!/usr/bin/env python
# -*- coding: utf-8 -*-

import builtins
import collections
import sys
import traceback


"""
Programming
Opdracht PROG: Bagagekluizen
(c) 2024 Hogeschool Utrecht,
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.
Lever je werk in op Canvas als alle tests slagen.
"""

# Dictionary die kluizen koppelt aan codes
kluizen = {
    "11": "6754",
    "1": "geheim",
    "5": "kluisvanpietje",
    "12": "z@terd@g",
}

def lees_kluizen():
    """Leest de kluizen uit het bestand en slaat ze op in een dictionary."""
    try:
        with open("kluizen.txt", "r") as bestand:
            kluizen = {}
            for regel in bestand:
                kluisnummer, code = regel.strip().split(';')
                kluizen[kluisnummer] = code
        return kluizen
    except FileNotFoundError:
        return {}

def schrijf_kluizen(kluizen):
    """Schrijft de huidige kluizen en codes naar het bestand."""
    with open("kluizen.txt", "w") as bestand:
        for kluisnummer, code in kluizen.items():
            bestand.write(f"{kluisnummer};{code}\n")

def aantal_kluizen_vrij():
    """Bepaal hoeveel kluizen nog vrij zijn (maximaal 12 kluizen)."""
    totaal_kluizen = 12
    kluizen = lees_kluizen()
    return totaal_kluizen - len(kluizen)

def nieuwe_kluis():
    """Voegt een nieuwe kluis toe met een door de gebruiker ingevoerde code."""
    kluizen = lees_kluizen()
    if len(kluizen) >= 12:
        return -2  # Geen kluizen meer beschikbaar

    beschikbare_kluizen =  [str(i) for i in range(1, 13) if str(i) not in kluizen]
    code = input("Voer een code in voor de kluis (minimaal 4 tekens, geen ';'): ")


    kluisnummer = beschikbare_kluizen[0]
    kluizen[kluisnummer] = code
    schrijf_kluizen(kluizen)
    return int(kluisnummer)

def kluis_openen():
    """Controleert of een kluisnummer en code geldig zijn voor toegang."""
    kluizen = lees_kluizen()
    kluisnummer = input("Voer je kluisnummer in: ")
    code = input("Voer je code in: ")

    if kluisnummer in kluizen and kluizen[kluisnummer] == code:
        return True
    return False

def kluis_teruggeven():
    """Verwijdert een kluisnummer en code uit het bestand."""
    kluizen = lees_kluizen()
    kluisnummer = input("Voer je kluisnummer in: ")
    code = input("Voer je code in: ")

    if kluisnummer in kluizen and kluizen[kluisnummer] == code:
        del kluizen[kluisnummer]
        schrijf_kluizen(kluizen)
        return True
    return False

def start_programma():
    """Toont het keuzemenu en verwerkt de gebruikerskeuze."""
    while True:
        Keuze = input("1: Ik wil weten hoeveel kluizen nog vrij zijn\n"
                      "2: Ik wil een nieuwe kluis\n"
                      "3: Ik wil even iets uit mijn kluis halen\n"
                      "4: Ik geef mijn kluis terug\n"
                      "5: Ik wil stoppen\n"
                      "Maak een keuze: \n")

        if Keuze == "1":
            print(f"Er zijn {aantal_kluizen_vrij()} kluizen vrij.\n")
        elif Keuze == "2":
            resultaat = nieuwe_kluis()
            if resultaat == -1:
                print("Ongeldige code. De code moet minimaal 4 tekens bevatten en geen ';' gebruiken.\n")
            elif resultaat == -2:
                print("Er zijn geen kluizen meer beschikbaar.\n")
            else:
                print(f"Je hebt kluis {resultaat} gekregen.\n")
        elif Keuze == "3":
            if kluis_openen():
                print("Kluis geopend.\n")
            else:
                print("Ongeldige combinatie van kluisnummer en code.\n")
        elif Keuze == "4":
            if kluis_teruggeven():
                print("Kluis teruggegeven.\n")
            else:
                print("Ongeldige combinatie van kluisnummer en code.\n")
        elif Keuze == "5":
            print("Programma gestopt.\n")
            break
        else:
            print("Ongeldige keuze, voer een geldig nummer in (1-5).\n")


if __name__ == "__main__":
    start_programma()

def module_runner():
    def module_runner():
        development_code()  # Comment deze regel om je 'development_code' uit te schakelen
        __run_tests()  # Comment deze regel om de HU-tests uit te schakelen

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


def __out_of_input_error():
    raise AssertionError("Fout: er werd in de functie vaker om input gevraagd dan verwacht.")


def __my_test_file():
    return "testkluizen.txt"


def __check_line_in_testfile(line, testfile=__my_test_file()):
    with open(testfile, 'r') as dummy_file:
        for file_line in dummy_file.readlines():
            if line.strip() == file_line.strip():
                return True

    return False


def __create_test_file(safes, testfile=__my_test_file()):
    kluis_mv_ev = 'kluis' if len(safes) == 1 else 'kluizen'
    print(f"Voor testdoeleinden wordt bestand {testfile} aangemaakt met {len(safes)} {kluis_mv_ev}... ", end="")

    try:
        with open(testfile, 'w') as dummy_file:
            for number, code in safes:
                dummy_file.write(f"{number};{code}\n")
    except:
        print(f"\nFout: bestand {testfile} kon niet worden aangemaakt. Python-error:")
        print(traceback.format_exc())
        sys.exit()

    print("Klaar.")


def __create_fake_open(original_open):
    def fake_open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        return original_open(__my_test_file(), mode=mode, buffering=buffering, encoding=encoding, errors=errors,
                      newline=newline, closefd=closefd, opener=opener)
    return fake_open


def test_aantal_kluizen_vrij():
    function = aantal_kluizen_vrij

    case = collections.namedtuple('case', 'safes')
    testcases = [case(((11, "6754"),)),
                 case(((11, "6754"), (1, "geheim"), (12, "z@terd@g"))),
                 case(((1, "0000"), (3, "0000"), (5, "0000"), (7, "0000"), (9, "0000"), (11, "0000"),
                       (2, "0000"), (4, "0000"), (6, "0000"), (8, "0000"), (10, "0000"), (12, "0000")))]

    for test in testcases:
        __create_test_file(test.safes)

        original_open = builtins.open
        builtins.open = __create_fake_open(original_open)

        try:
            expected_output = 12 - len(test.safes)
            __my_assert_args(function, (), expected_output, check_type=True)
        finally:
            builtins.open = original_open


def test_nieuwe_kluis():
    function = nieuwe_kluis

    case = collections.namedtuple('case', 'safes simulated_input possible_outputs clean_context')
    testcases = [case(((1, "0000"), (3, "0000"), (5, "0000"), (7, "0000"), (9, "0000"), (11, "0000"), (2, "0000"),
                       (4, "0000"), (6, "0000"), (8, "0000"), (10, "0000"), (12, "0000")), ["geheim"], [-2], True),
                 case(((1, "0000"), (3, "0000"), (5, "0000"), (7, "0000"), (9, "0000"), (11, "0000"),
                       (2, "0000"), (4, "0000"), (6, "0000"), (8, "0000"), (12, "0000")), ["geheim"], [10], True),
                 case(((1, "0000"), (3, "0000"), (5, "0000"), (8, "0000"), (10, "0000"), (12, "0000"),
                       (2, "0000"), (4, "0000"), (6, "0000"), (9, "0000"), (11, "0000")), ["geheim"], [7], True),
                 case(((2, "0000"), (4, "0000"), (6, "0000"), (8, "0000"), (10, "0000"), (12, "0000"),
                       (3, "0000"), (5, "0000"), (7, "0000"), (9, "0000"), (11, "0000")), ["geheim"], [1], True),
                 case(((1, "0000"), (3, "0000")), ["abc"], [-1], True),
                 case(((1, "0000"), (3, "0000")), ["geheim;"], [-1], True),
                 case(((11, "6754"), (12, "z@terd@g")), ["geheim"], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True),
                 # extra test to check whether adding a new safe twice will succeed
                 case(((11, "6754"), (12, "z@terd@g"), (None, "onbekend")), # thirth (unknown) safe, from previous test
                      ["geheim"], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False)]  # use testfile from previous test

    for test in testcases:
        if test.clean_context:
            __create_test_file(test.safes)
        else:
            print(f"Voor testdoeleinden wordt bestand {__my_test_file()} nogmaals gebruikt.")





