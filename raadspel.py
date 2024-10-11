# Vebeterpunten:
# - Haal onnodig comments weg
# - zorg dat je game opnieuwe weer start
# - zorg dat je communicatie met de user duidelijker is
# - gebruik de /n op nieuwe regel aan te maken
# - gebruik kleur code op je spelletje leuker te ma

import random

# Bij deze stap groet ik de user en vraag ik of ze klaar zijn om te spellen.
def guess_number():

    print("Welcome to the win the number game, are you ready? (yes or no)")

    ready = input().strip().lower()
    # Met deze stap kan ik bepalen wat ik moet zeggen als de user "nee" aangeeft op vraag of ze willen spellen.
    if ready == "no":

        print("Alright, that is fine. See you next time!")
        return
    #Met deze stap kan ik bepalen wat ik moet zeggen als de user "ja" als antwoord geeft op mijn vraag of ze willen spellen.
    if ready == "yes":
        print("Yay, let's play the game")
        # In het volgende stuk van 17 tot met 19 leg ik de user uit wat de regels zijn en wat ik ga betekenen voor hun in het spel.
        # Important information!
        print("But before you play, I have important information you must remember!")
        print("You can only guess 5 times; if you run out of chances, the game will end.")
        print("Each guess I will let you know if the number is too high or too low.")
        # Bij het volgende stukje vraag ik de user om een getal te raden binnen een bepaalde range.
        print("Try to guess a number between 1 & 50")

        random_number = random.randint(1, 50) # Met deze functie zal de systeem ervoor zorgen dat de raadnummer tussen de 1 en 50 zal blijven en dat het hier tussen willekeurig uitgekozen worden.
        max_attempts = 5 # Met deze functie zal de maximaal pogingen op 5 belijven.
# Met deze functie word ervoor gezorgd dat de loop tot maximaal 5 poging loopt.
        for attempt in range(max_attempts):
            try:
                guess = int(input("Please enter the number: ")) # Met deze functie vraag ik de user om het getal in te voeren.                 # Met deze functie zal het systeem controleren of de ingevoerde getal gelijk is aan de willekeurig getal van het systeem.
                if guess < random_number: # Met dit stukje laat ik de user weten dat het getal dat ze hebben ingevoerd te hoog is bij 31.
                    print("Oops, it's too low. Try again!")
                elif guess > random_number: # Met dit stukje laat ik de user weten dat het getal dat ze hebben ingevoerd te hoog is.
                    print("Oops, it's too high. Try again!")
                else: # Met dit stukje feliciteer ik de user als ze juist antwoord hebben.
                    print("Yay, you guessed it right. Good job!")
                    break # met deze functie zal het speletje stoppen als de user het goed heeft geraden.
#
            except ValueError:
                print("Please enter a valid number.")
# Als alle kansen op zijn zal de user het volgende krijgen:
        else:
            print("Oh no, you have used all your chances! The correct number was:", random_number)
# Als de user iets verkeerd invult anders dan "ja" en "nee" krijgen ze deze tekst.
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")
        guess_number()


# main
guess_number()
