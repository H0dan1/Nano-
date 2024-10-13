import json
import os
from datetime import datetime

# Bestand voor het dagboek
DAGBOEK_BESTAND = "Dagboek.json"

# Voeg horizontale lijnen toe voor visuele scheiding
def print_scheiding():
    print("-" * 40)

# Als het dagboekbestand niet bestaat, maak het aan
if not os.path.exists(DAGBOEK_BESTAND):
    with open(DAGBOEK_BESTAND, "w") as f:
        json.dump({}, f)

# Dagboek openen
def open_dagboek():
    print_scheiding()
    with open(DAGBOEK_BESTAND, "r") as f:
        return json.load(f)

# Dagboek opslaan
def opslaan_dagboek_op(dagboek):
    print_scheiding()
    with open(DAGBOEK_BESTAND, "w") as f:
        json.dump(dagboek, f, indent=4)

# Toevoegen aan dagboek
def toevoegen_dagboek(datum, tekst):
    print_scheiding()
    dagboek = open_dagboek()
    if datum in dagboek:
        keuze = input(f"Helaas is er al een toevoeging voor {datum}. Wil je het opnieuw herschrijven? (ja/nee) ")
        if keuze.lower() != "ja":
            return
    dagboek[datum] = tekst
    opslaan_dagboek_op(dagboek)
    print(f"Dagboek voor {datum} is up to date!")

# Dagboekvermelding lezen
def lees_dagboek_vermelding(datum):
    print_scheiding()
    dagboek = open_dagboek()
    if datum in dagboek:
        print(f"Dagboek voor {datum}: {dagboek[datum]}")
    else:
        print(f"Geen dagboekvermelding gevonden voor {datum}.")

# Dagboekvermelding wijzigen
def wijzing_dagboek(datum):
    print_scheiding()
    dagboek = open_dagboek()
    if datum in dagboek:
        nieuwe_tekst = input(f"Voer de nieuwe tekst in voor {datum}: ")
        dagboek[datum] = nieuwe_tekst
        opslaan_dagboek_op(dagboek)
        print(f"Dagboek voor {datum} is up to date!")
        print_scheiding()
    else:
        print(f"Helaas geen dagboekvermeldingen voor {datum}.")

# Vragen naar de datum
def vraag_datum():
    print_scheiding()
    keuze = input("Wil je de invoer voor vandaag of een andere datum? [Vandaag - Andere datum] ").lower()
    if keuze == "vandaag":
        return datetime.today().strftime("%d-%m-%Y")
    else:
        return input("Voer de datum in (formaat: DD-MM-YYYY): ")

# Wachtwoordverificatie
def vraag_wachtwoord():
    print_scheiding()
    correct_wachtwoord = "Hodan"

    while True:
        ingevoerd_wachtwoord = input("Voer je wachtwoord in: ")
        if ingevoerd_wachtwoord == correct_wachtwoord:
            print("Toegang verleend tot het dagboek.")
            break
        else:
            print("Onjuist wachtwoord, probeer het opnieuw.")

# Hoofdprogramma
def main():
    vraag_wachtwoord()  # Wachtwoordverificatie voor toegang tot het dagboek

    while True:
        print_scheiding()
        print("Maak een keuze uit de volgende opties [1 - 4]:")
        print("1 - Voeg een dagboekvermelding toe.")
        print("2 - Lees een dagboekvermelding.")
        print("3 - Bewerk een dagboekvermelding.")
        print("4 - Verlaat het dagboek.")

        keuze = input("Jouw keuze: ")
        print_scheiding()

        if keuze == "1":
            datum = vraag_datum()
            tekst = input(f"Voer de tekst in voor {datum}: ")
            toevoegen_dagboek(datum, tekst)
        elif keuze == "2":
            datum = vraag_datum()
            lees_dagboek_vermelding(datum)
        elif keuze == "3":
            datum = vraag_datum()
            wijzing_dagboek(datum)
        elif keuze == "4":
            print("Dagboek wordt afgesloten.")
            return
        else:
            print("Ongeldige keuze, probeer het opnieuw.")

# Start het programma
if __name__ == "__main__":
    main()
















