# ============================================================
# main.py - Entry point of the application
# Displays the main menu and routes user choices to GareRoutiere
# ============================================================

from gare import GareRoutiere

# ---- Visual separator for the menu ----
SEPARATOR = "=" * 54


def display_menu():
    """Display the main menu options to the user."""
    print(f"\n{SEPARATOR}")
    print("       TICKET NANA - BUS RESERVATION SYSTEM")
    print(SEPARATOR)
    print("  1. Book a ticket")
    print("  2. View my reservations")
    print("  3. Cancel a reservation")
    print("  0. Quit")
    print(SEPARATOR)


def main():
    """Run the main application loop until the user chooses to quit."""
    # ---- Create the main application object (loads existing reservations) ----
    gare = GareRoutiere()

    # ---- Welcome message with key info ----
    print(f"\n{SEPARATOR}")
    print("       TICKET NANA - BUS RESERVATION SYSTEM")
    print(SEPARATOR)
    print("  Cities served : Ouagadougou | Koudougou | Bobo-Dioulasso")
    print("  Departure times: 06:00 | 13:00 | 20:00")
    print("  Seats per bus  : 30")
    print(SEPARATOR)

    while True:
        display_menu()
        choice = input("  Your choice: ").strip()

        # ---- Route the choice to the appropriate method ----
        if choice == "1":
            gare.book_ticket()

        elif choice == "2":
            gare.view_reservations()

        elif choice == "3":
            gare.cancel_reservation()

        elif choice == "0":
            # ---- Exit the application ----
            print("\n  Thank you for using Ticket Nana. Safe travels!")
            print(f"{SEPARATOR}\n")
            break

        else:
            # ---- Handle invalid menu input ----
            print("  [!] Invalid choice. Please enter 0, 1, 2 or 3.")


# ---- Run the application only if this file is executed directly ----
if __name__ == "__main__":
    main()
    # ---- Keep the window open after the program ends ----
    input("\n  Press Enter to close...")
