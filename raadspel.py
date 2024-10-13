import random
from colorama import Fore, Style, init


def start_game():
    print("Begin het raadspel!")

init()

def print_title():
    title = "WIN THE NUMBER GAME"
    print("\n" + "=" * 40)
    print(Fore.MAGENTA + title.center(40) + Style.RESET_ALL)
    print("=" * 40 + "\n")


def guess_number():
    print_title()

    print(Fore.MAGENTA + "BEN JE KLAAR OM TE SPELEN? JA OF NEE" + Style.RESET_ALL)

    ready = input().strip().lower()
    print("\n")

    if ready == "nee":
        print(Fore.WHITE + "Geen probeleem, Tot de volgende keer!" + Style.RESET_ALL)
        return

    if ready == "ja":
        print(Fore.YELLOW + "=" * 40)
        print("Voordat we spelen, hier is wat informatie over het spel:\n")
        print("Bij 'WIN THE NUMBER GAME' heb je in totaal 6 kansen om een nummer tussen 1 en 50 te raden.")
        print("Het spel laat je weten of het nummer te hoog of te laag is en hoeveel kansen je nog over hebt.")
        print("Aan het einde van het spel heb je de optie om opnieuw te spelen of te stoppen.\n")
        print("Veel succes met het spel en veel plezier!\n")
        print("=" * 40 + Style.RESET_ALL + "\n")

        while True:
            random_number = random.randint(1, 50)
            max_attempts = 6
            attempt = 0

            while attempt < max_attempts:
                try:
                    guess = int(input(
                        Fore.MAGENTA + "Voer een nummer tussen 1 en 50 in: " + Style.RESET_ALL))

                    if guess < 1 or guess > 50:
                        print(Fore.RED + "Ongeldig nummer. Voer een nummer tussen 1 en 50 in." + Style.RESET_ALL)
                        print("\n")
                        continue


                    if guess < random_number:
                        attempt += 1
                        remaining_attempts = max_attempts - attempt
                        print(Fore.MAGENTA + f"Te laag! Je hebt {remaining_attempts} kansen over." + Style.RESET_ALL)
                    elif guess > random_number:
                        attempt += 1
                        remaining_attempts = max_attempts - attempt
                        print(Fore.MAGENTA + f"Te hoog! Je hebt {remaining_attempts} kansen over." + Style.RESET_ALL)
                    else:
                        print(Fore.MAGENTA + "Gefeliciteerd! Je hebt het juiste nummer geraden!" + Style.RESET_ALL)
                        break

                    print("\n" + "-" * 40 + "\n")

                except ValueError:
                    print(Fore.RED + "Voer alstublieft een geldig geheel getal in." + Style.RESET_ALL)
                    print("\n")
                    continue

            else:
                print(Fore.RED + f"Spel afgelopen! Je hebt al je kansen gebruikt. Het juiste nummer was: {random_number}" + Style.RESET_ALL)

            print("\n" + "=" * 40 + "\n")


            while True:
                print(Fore.MAGENTA + "Wil je opnieuw spelen? (1 voor Ja, 2 voor Nee): " + Style.RESET_ALL)
                play_again = input().strip()

                if play_again == "1":
                    break
                elif play_again == "2":
                    print(Fore.YELLOW + "Bedankt voor het spelen! Tot ziens!" + Style.RESET_ALL)
                    return
                else:
                    print(Fore.RED + "Ongeldige invoer. Kies '1' voor Ja of '2' voor Nee." + Style.RESET_ALL)
                    print("\n")

    else:
        print(Fore.RED + "Ongeldige reactie. Voer 'ja' of 'nee' in." + Style.RESET_ALL)
        guess_number()



guess_number()




