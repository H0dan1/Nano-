

DAGBOEK_BESTAND = "Dagboek.json"

from colorama import Fore, Style, init
import os, json
from datetime import datetime
 # Initialize colorama
init()





# Voeg horizontale lijnen toe voor visuele scheiding (blauw)
def print_scheiding():
    print(Fore.GREEN + "-" * 40 + Style.RESET_ALL)

# Als het dagboekbestand niet bestaat, maak het aan
if not os.path.exists(DAGBOEK_BESTAND):
    with open(DAGBOEK_BESTAND, "w") as f:
        json.dump({}, f)

# Dagboek openen
def open_dagboek():
    print_scheiding()
    try:
        with open(DAGBOEK_BESTAND, "r") as f:
            inhoud = f.read().strip()  # Verwijder onnodige spaties en nieuwe regels
            if not inhoud:  # Controleer of het bestand leeg is
                return {}  # Als het leeg is, geef een lege dictionary terug
            return json.loads(inhoud)  # Als het niet leeg is, laad de JSON-data
    except FileNotFoundError:
        # Als het bestand niet bestaat, maak een leeg dagboek aan
        return {}



# Dagboek opslaan (blauw)
def opslaan_dagboek_op(dagboek):
    print_scheiding()
    with open(DAGBOEK_BESTAND, "w") as f:
        json.dump(dagboek, f, indent=4)

# Toevoegen aan dagboek (blauw met rood voor waarschuwing)
def toevoegen_dagboek(datum, tekst):
    print_scheiding()
    dagboek = open_dagboek()
    if datum in dagboek:
        keuze = input(Fore.RED + f"Helaas is er al een toevoeging voor {datum}. Wil je het opnieuw herschrijven? (ja/nee) " + Style.RESET_ALL)
        if keuze.lower() != "ja":
            return
    dagboek[datum] = tekst
    opslaan_dagboek_op(dagboek)
    print(Fore.BLUE + f"Dagboek voor {datum} is up to date!" + Style.RESET_ALL)

# Dagboekvermelding lezen en opties geven als er geen vermelding is
def lees_dagboek_vermelding(datum):
    print_scheiding()
    dagboek = open_dagboek()
    if datum in dagboek:
        print(Fore.BLUE + f"Dagboek voor {datum}: {dagboek[datum]}" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Helaas, geen dagboekvermelding gevonden voor {datum}." + Style.RESET_ALL)
        keuze = input(Fore.BLUE + "Wil je een nieuwe vermelding schrijven? (ja/nee) of een andere datum proberen? (andere datum): " + Style.RESET_ALL).lower()
        if keuze == "ja":
            tekst = input(Fore.BLUE + f"Voer de tekst in voor {datum}: " + Style.RESET_ALL)
            toevoegen_dagboek(datum, tekst)
        elif keuze == "andere datum":
            nieuwe_datum = vraag_datum()  # Vraag om een nieuwe datum
            lees_dagboek_vermelding(nieuwe_datum)  # Probeer opnieuw met de nieuwe datum
        else:
            print(Fore.RED + "Geen nieuwe dagboekvermelding toegevoegd." + Style.RESET_ALL)


# Dagboekvermelding wijzigen (blauw met rood voor geen vermelding)
def wijzing_dagboek(datum):
    print_scheiding()
    dagboek = open_dagboek()
    if datum in dagboek:
        nieuwe_tekst = input(Fore.BLUE + f"Voer de nieuwe tekst in voor {datum}: " + Style.RESET_ALL)
        dagboek[datum] = nieuwe_tekst
        opslaan_dagboek_op(dagboek)
        print(Fore.BLUE + f"Dagboek voor {datum} is up to date!" + Style.RESET_ALL)
        print_scheiding()
    else:
        print(Fore.RED + f"Helaas geen dagboekvermeldingen voor {datum}." + Style.RESET_ALL)


# Vragen naar de datum
def vraag_datum():
    print_scheiding()
    while True:  # Herhaal tot een geldige invoer is ontvangen
        keuze = input(Fore.BLUE + "Wil je de invoer voor vandaag of een andere datum? [Vandaag - Andere datum] " + Style.RESET_ALL).lower()
        if keuze == "vandaag":
            return datetime.today().strftime("%d-%m-%Y")
        elif keuze == "andere datum":
            return input(Fore.BLUE + "Voer de datum in (formaat: DD-MM-YYYY): " + Style.RESET_ALL)
        else:
            print(Fore.RED + "Ongeldige invoer. Kies 'Vandaag' of 'Andere datum'." + Style.RESET_ALL)
            terug_keuze = input(Fore.BLUE + "Wil je terug naar het menu of opnieuw proberen? [Terug - Opnieuw] ").lower()
            if terug_keuze == "terug":
                return None  # Geef None terug om aan te geven dat ze terug willen


def vraag_wachtwoord():
    print_scheiding()
    correct_wachtwoord = "1234"

    while True:
        ingevoerd_wachtwoord = input(Fore.BLUE + "Voer je wachtwoord in: " + Style.RESET_ALL)
        if ingevoerd_wachtwoord == correct_wachtwoord:
            print(Fore.BLUE + "Toegang verleend" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Toegang niet verleend, probeer het opnieuw" + Style.RESET_ALL)


# Hoofdprogramma (blauw)
def main():
    vraag_wachtwoord()
    while True:
        print_scheiding()
        print(Fore.BLUE + "Maak een keuze uit de volgende opties [1 - 4]:" + Style.RESET_ALL)
        print("1 - Voeg een dagboekvermelding toe.")
        print("2 - Lees een dagboekvermelding.")
        print("3 - Bewerk een dagboekvermelding.")
        print("4 - Verlaat het dagboek.")

        keuze = input(Fore.BLUE + "Jouw keuze: " + Style.RESET_ALL)
        print_scheiding()

        if keuze == "1":
            datum = vraag_datum()
            tekst = input(Fore.BLUE + f"Voer de tekst in voor {datum}: " + Style.RESET_ALL)
            toevoegen_dagboek(datum, tekst)
        elif keuze == "2":
            datum = vraag_datum()
            lees_dagboek_vermelding(datum)
        elif keuze == "3":
            datum = vraag_datum()
            wijzing_dagboek(datum)
        elif keuze == "4":
            print(Fore.BLUE + "Dagboek wordt afgesloten." + Style.RESET_ALL)
            return
        else:
            print(Fore.RED + "Ongeldige keuze, probeer het opnieuw." + Style.RESET_ALL)

# Start het programma
if __name__ == "__main__":
    main()
