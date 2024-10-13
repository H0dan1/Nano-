
DAGBOEK_BESTAND = "Dagboek.json"

from colorama import Fore, Style, init
import os, json
from datetime import datetime


init()

def start_Dagboek():
    print("Welkom bij Mijn health notes!")


    def print_titel():
        print(Fore.CYAN + "\n" + "=" * 40 + "\n            MIJN HEALTH NOTES   \n" + "=" * 40 + Style.RESET_ALL)

    def print_scheiding():
        print("\n" + "_" * 40 + "\n")


    if not os.path.exists(DAGBOEK_BESTAND):
        with open(DAGBOEK_BESTAND, "w") as f:
            json.dump({}, f)

    # Dagboek openen
    def open_dagboek():
        print_scheiding()
        try:
            with open(DAGBOEK_BESTAND, "r") as f:
                inhoud = f.read().strip()
                if not inhoud:
                    return {}
                return json.loads(inhoud)
        except FileNotFoundError:
            return {}


    def opslaan_dagboek_op(dagboek):
        print_scheiding()
        with open(DAGBOEK_BESTAND, "w") as f:
            json.dump(dagboek, f, indent=4)

    def toevoegen_dagboek(datum, keuze_gezondheid, tekst):
        print_scheiding()
        dagboek = open_dagboek()
        if datum in dagboek:
            print(Fore.RED + f"Helaas is er al een toevoeging voor deze {datum}." + Style.RESET_ALL)
            return
        dagboek[datum] = {
            'keuze': keuze_gezondheid,
            'tekst': tekst
        }
        opslaan_dagboek_op(dagboek)
        print(Fore.BLUE + f"Health notes voor {datum} is toegevoegd!" + Style.RESET_ALL)

    def lees_dagboek_vermelding(datum):
        dagboek = open_dagboek()
        if datum in dagboek:
            print(Fore.BLUE + f"Notes voor {datum}:" + Style.RESET_ALL)

            keuze = dagboek[datum]['keuze']
            antwoorden = dagboek[datum]['tekst']
            keuze_str = "Mentale gezondheid" if keuze == "1" else "Lichamelijke gezondheid"
            print(Fore.CYAN + f"Keuze: {keuze_str}" + Style.RESET_ALL)

            vragen = [
                "Hoe voel je je vandaag?",
                "Heb je stress ervaren?",
                "Wat heeft je vandaag gelukkig gemaakt?" if keuze == "1" else "Hoe voel je je lichamelijk vandaag?"
            ]

            for vraag, antwoord in zip(vragen, antwoorden):
                if antwoord:
                    print(f"{vraag} - {antwoord}")
        else:
            print(Fore.RED + f"Er is helaas geen notes gevonden voor {datum}." + Style.RESET_ALL)
            while True:
                keuze = input(
                    Fore.BLUE + "Wil je een nieuwe health notes schrijven? (ja/nee): " + Style.RESET_ALL).lower()
                if keuze == "ja":
                    tekst, keuze_gezondheid = vragen_keuze()
                    toevoegen_dagboek(datum, keuze_gezondheid, tekst)
                    break
                elif keuze == "nee":
                    print(Fore.BLUE + "\nJe bent terug bij het menu keuze." + Style.RESET_ALL)
                    break
                else:
                    print(Fore.RED + "Ongeldige keuze, probeer opnieuw." + Style.RESET_ALL)

    def wijzig_dagboek(datum):
        print_scheiding()
        dagboek = open_dagboek()
        if datum in dagboek:
            keuze = dagboek[datum]['keuze']
            keuze_str = "Mentale gezondheid" if keuze == "1" else "Lichamelijke gezondheid"
            print(Fore.BLUE + f"Huidige keuze: {keuze_str}" + Style.RESET_ALL)

            oude_tekst = dagboek[datum]['tekst']
            print(Fore.BLUE + f"Huidige tekst voor {datum}:" + Style.RESET_ALL)

            # Toon oude antwoorden met bijbehorende vragen
            print(Fore.CYAN + "Oude antwoorden:" + Style.RESET_ALL)
            for i, antwoord in enumerate(oude_tekst):
                if antwoord:
                    print(f"{oude_tekst[i]}")

            keuze_gezondheid = keuze
            print(Fore.BLUE + "Je kunt alleen de antwoorden voor de eerder gemaakte keuze wijzigen." + Style.RESET_ALL)

            if keuze_gezondheid == "1":
                tekst = vragen_gezondheid(oude_tekst)
            elif keuze_gezondheid == "2":
                tekst = vragen_lichamelijke_gezondheid()

            dagboek[datum] = {
                'keuze': keuze_gezondheid,
                'tekst': tekst
            }
            opslaan_dagboek_op(dagboek)
            print(Fore.BLUE + f"Jouw notes is geüpdated voor {datum}!" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Helaas is er geen notes voor deze {datum}." + Style.RESET_ALL)

    # Vragen naar de gezondheid
    def vragen_gezondheid():
        vragen = [
            "Hoe voel je je vandaag?",
            "Heb je stress ervaren?",
            "Waar ben je dankbaar voor vandaag?"
        ]
        antwoorden = []

        print(Fore.CYAN + "Je hebt gekozen voor mentale gezondheid." + Style.RESET_ALL)
        for vraag in vragen:
            antwoord = input(Fore.BLUE + vraag + " " + Style.RESET_ALL)
            antwoorden.append(antwoord)

        print(Fore.GREEN + "Dit was het einde van de drie vragen." + Style.RESET_ALL)

        return antwoorden

    def vragen_lichamelijke_gezondheid():
        vragen = [
            "Hoe voel je je lichamelijk vandaag?",
            "Heb je voldoende beweging gehad?",
            "Heb je voldoende gegeten?"
        ]
        antwoorden = []

        print(Fore.CYAN + "Je hebt gekozen voor lichamelijke gezondheid." + Style.RESET_ALL)
        for vraag in vragen:
            antwoord = input(Fore.BLUE + vraag + " " + Style.RESET_ALL)
            antwoorden.append(antwoord)

        print(Fore.GREEN + "Dit was het einde van de drie vragen." + Style.RESET_ALL)

        return antwoorden

    def vragen_keuze():
        print(Fore.BLUE + "Kies een type gezondheid:\n1. Mentale gezondheid\n2. Lichamelijke gezondheid" + Style.RESET_ALL)
        while True:
            keuze = input(Fore.BLUE + "Maak een keuze (1 of 2): " + Style.RESET_ALL)
            if keuze in ["1", "2"]:
                if keuze == "1":
                    return vragen_gezondheid([]), keuze
                else:
                    return vragen_lichamelijke_gezondheid(), keuze
            else:
                print(Fore.RED + "Ongeldige keuze. Probeer het opnieuw." + Style.RESET_ALL)

    def vraag_datum():
        while True:
            keuze = input(Fore.BLUE + "Wil je de invoer voor (1) Vandaag of (2) Andere datum? " + Style.RESET_ALL).strip()
            if keuze == "1":
                return datetime.today().strftime("%d-%m-%Y")
            elif keuze == "2":
                return input(Fore.BLUE + "Voer de datum in (formaat: dag-maand-jaar): " + Style.RESET_ALL)
            else:
                print(Fore.RED + "Ongeldige invoer. Kies '1' voor Vandaag of '2' voor Andere datum." + Style.RESET_ALL)

    def vraag_wachtwoord():
        print_scheiding()
        correct_wachtwoord = "1234"

        while True:
            ingevoerd_wachtwoord = input(Fore.BLUE + "Voer je wachtwoord in: " + Style.RESET_ALL)
            if ingevoerd_wachtwoord == correct_wachtwoord:
                print(Fore.GREEN + "Toegang verleend!" + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "Ongeldig wachtwoord. Probeer het opnieuw." + Style.RESET_ALL)

    while True:
        print_titel()
        vraag_wachtwoord()
        while True:
            print_scheiding()
            print(Fore.BLUE + "Maak een keuze uit de volgende optie's [ 1 - 4 ]:\n"
                              "1. Health notes toevoegen\n"
                              "2. Health notes lezen\n"
                              "3. Health notes wijzigen\n"
                              "4. Afsluiten" + Style.RESET_ALL)
            keuze = input(Fore.BLUE + "Maak een keuze (1-4): " + Style.RESET_ALL)

            if keuze == "1":
                    datum = vraag_datum()
                    tekst, keuze_gezondheid = vragen_keuze()
                    toevoegen_dagboek(datum, keuze_gezondheid, tekst)

            elif keuze == "2":
                    datum = input(Fore.BLUE + "Voer de datum in voor de health notes die je wilt lezen: " + Style.RESET_ALL)
                    lees_dagboek_vermelding(datum)

            elif keuze == "3":
                    datum = input(Fore.BLUE + "Voer de datum in voor de health notes die je wilt wijzigen: " + Style.RESET_ALL)
                    wijzig_dagboek(datum)

            elif keuze == "4":
                    print(Fore.GREEN + "Bedankt voor het gebruik van Mijn Health Notes!" + Style.RESET_ALL)
                    return

            else:
                    print(Fore.RED + "Ongeldige keuze, probeer opnieuw." + Style.RESET_ALL)


start_Dagboek()

