# Dictionary van kluizen met codes en status ervan.
kluizen = {
    "1": ("geheim", "beschikbaar"),
    "2": ("", "beschikbaar"),
    "3": ("", "beschikbaar"),
    "4": ("", "beschikbaar"),
    "5": ("kluisvanpietje", "beschikbaar"),
    "6": ("", "beschikbaar"),
    "11": ("6754", "beschikbaar"),
    "12": ("z@terd@g", "beschikbaar"),
}


def lees_kluizen():
    return kluizen


def schrijf_kluizen():
    pass


def schrijf_gebruikersdata(kluisnummer, wachtwoord):
    try:
        with open('kluizen.txt', 'a') as bestand:
            bestand.write(f"Kluisnummer: {kluisnummer}, Wachtwoord: {wachtwoord}\n")
    except Exception as e:
        print(f"Fout bij het schrijven naar het bestand: {e}")


def kluis_openen():
    kluizen_data = lees_kluizen()
    kluisnummer = input("Voer uw kluisnummer in: ")

    if kluisnummer in kluizen_data:
        code, status = kluizen_data[kluisnummer]
        if status.strip() == 'beschikbaar':
            gebruikerscode = input(f"Voer de code voor kluis {kluisnummer} in: ")
            if gebruikerscode == code:
                kluizen[kluisnummer] = (code, 'bezet')  # Markeer de kluis als bezet
                schrijf_gebruikersdata(kluisnummer, gebruikerscode)  # Schrijf de gegevens naar het bestand
                print(f"Kluis {kluisnummer} is geopend.")
                return True
            else:
                print("Ongeldige code. Toegang geweigerd.")
                return False
        else:
            print(f"Kluis {kluisnummer} is niet beschikbaar.")
            return False
    else:
        print("Kluisnummer niet gevonden.")
        return False


def nieuwe_kluis():
    print("Er is geen mogelijkheid om een nieuwe kluis toe te voegen in deze versie.")


def kluis_teruggeven():
    kluisnummer = input("Voer uw kluisnummer in die u wilt teruggeven: ")
    if kluisnummer in kluizen:
        code, status = kluizen[kluisnummer]
        if status.strip() == 'bezet':
            kluizen[kluisnummer] = (code, 'beschikbaar')
            print(f"Kluis {kluisnummer} is teruggegeven.")
            return
        else:
            print(f"Kluis {kluisnummer} is al beschikbaar.")
            return
    else:
        print("Kluisnummer niet gevonden.")

# Hier staan de keuze menu, waarvan de user van kan kijken.
def start_programma():
    while True:
        print("\nKies een optie:")
        print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
        print("2: Ik wil een nieuwe kluis")
        print("3: Ik wil even iets uit mijn kluis halen")
        print("4: Ik geef mijn kluis terug")
        print("5: Ik wil stoppen")
        keuze = input("Maak een keuze: ")

        # In de volgende functie staat alle gebruikerskeuze en de kluizen die verhuurd kunnen worden.
        if keuze == '1':
            vrij_aantal = sum(1 for _, status in kluizen.values() if status.strip() == 'beschikbaar')
            print(f"Aantal vrije kluizen: {vrij_aantal}")
        elif keuze == '2':
            nieuwe_kluis()
        elif keuze == '3':
            kluis_openen()
        elif keuze == '4':
            kluis_teruggeven()
        elif keuze == '5':
            print("Programma gestopt.")
            break
        else:
            print("Ongeldige keuze, probeer het opnieuw.")


# Start het programma
if __name__ == "__main__":
    start_programma()
