def display_menu():
    print(f"\n{SEPARATOR}")
    print("       TICKET NANA - BUS RESERVATION SYSTEM")
    print(SEPARATOR)
    print("  1. Book a ticket")
    print("  2. View my reservations")
    print("  3. Cancel a reservation")
    print("  0. Quit")
    print(SEPARATOR)

def main():
  gare = GareRoutiere()

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

   if choice == "1":
            gare.book_ticket()

elif choice == "2":
            gare.view_reservations()

  elif choice == "3":
            gare.cancel_reservation()

elif choice == "0":

print("\n  Thank you for using Ticket Nana. Safe travels!")
            print(f"{SEPARATOR}\n")
            break
 else:
  print("  [!] Invalid choice. Please enter 0, 1, 2 or 3.")
 if __name__ == "__main__":
    main()

 input("\n  Press Enter to close...")
