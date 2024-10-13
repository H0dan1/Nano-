from rich.console import Console
from rich.table import Table
from rich.text import Text
from colorama import Fore, Style

console = Console()

def main_menu():
    while True:
        console.clear()


        console.print("=" * 40, justify="center", style="bold magenta")
        title = Text("Time Off", style="bold magenta")  # Titel kleur en stijl
        console.print(title, justify="center", style="bold yellow on black")
        console.print("=" * 40, justify="center", style="bold magenta")

        # Korte beschrijving
        description = Text("Een leuke app met een raadspel en een gezondheidsdagboek!", style="bold white")
        console.print(description, justify="center")



        table1 = Table(show_header=False, border_style="orange3", width=50)
        table1.add_column("Optie", justify="center", style="bold white")
        table1.add_row(Fore.RED + "1. Win the number game" + Style.RESET_ALL)
        table1.add_row("Raad het juiste nummer tussen 1 - 50!")
        console.print(table1, justify="center")


        table2 = Table(show_header=False, border_style="orange3", width=50)
        table2.add_column("Optie", justify="center", style="bold white")
        table2.add_row(Fore.RED + "2. Mijn gezondheidsnotities" + Style.RESET_ALL)
        table2.add_row("Schrijf iets in je gezondheidsnotities!")
        console.print(table2, justify="center")


        table3 = Table(show_header=False, border_style="orange3", width=50)
        table3.add_column("Optie", justify="center", style="bold white")
        table3.add_row(Fore.RED + "3. Sluit Time off" + Style.RESET_ALL)
        console.print(table3, justify="center")




        choice = input(Fore.GREEN + "Voer je keuze in [ 1 - 2 - 3 ]: " + Style.RESET_ALL)

        if choice == '1':
            import raadspel
            raadspel.start_game()
        elif choice == '2':
            import Dagboek
            Dagboek.start_Dagboek()
        elif choice == '3':
            print(Fore.YELLOW + "Bedankt voor het spelen! Tot de volgende keer." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Ongeldige keuze, probeer het opnieuw." + Style.RESET_ALL)

if __name__ == "__main__":
    main_menu()

#einde