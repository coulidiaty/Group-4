#=================================================================================#
# ================SADIA'S PART START===================
#=================================================================================#
# gare.py - GareRoutiere class: core business logic
# Handles all operations: loading, booking, viewing, cancelling
# 
import os
from trajet      import Trajet
from ticket      import TicketStandard
from reservation import Reservation
from utils       import (generate_id, validate_date, validate_phone,
                         validate_not_empty, get_valid_input, get_valid_choice)

# ---- Application constants ----
RESERVATIONS_FILE = "reservations.txt"
MAX_SEATS         = 30
HORAIRES          = ["06:00", "13:00", "20:00"]

# ---- Define all available routes (both directions) ----
TRAJETS = [
    Trajet("Ouagadougou",    "Bobo-Dioulasso", 8000),
    Trajet("Bobo-Dioulasso", "Ouagadougou",    8000),
    Trajet("Koudougou",      "Bobo-Dioulasso", 6000),
    Trajet("Bobo-Dioulasso", "Koudougou",      6000),
    Trajet("Koudougou",      "Ouagadougou",    2000),
    Trajet("Ouagadougou",    "Koudougou",      2000),
]

SEPARATOR = "=" * 54
BACK      = "b"   # Keyword the user types to go back one step


class GareRoutiere:
    """
    Main class of the application.
    Manages the list of reservations and all user-facing operations.
    """

    def __init__(self):
        # ---- Load existing reservations from file on startup ----
        self.reservations = self.load_reservations()



        

    # OPERATIONS
    
    # ---- Read reservations.txt and rebuild the reservations list ----
    def load_reservations(self):
        reservations = []
        if not os.path.exists(RESERVATIONS_FILE):
            return reservations

        with open(RESERVATIONS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) != 9:
                    continue

                res_id, first_name, last_name, phone, dep, arr, price, date, horaire = parts
                trajet      = Trajet(dep, arr, int(price))
                ticket      = TicketStandard(trajet, date, horaire)
                reservation = Reservation(res_id, first_name, last_name, phone, ticket)
                reservations.append(reservation)

        return reservations
  # ---- Write all current reservations back to the file ----
    def save_reservations(self):
        with open(RESERVATIONS_FILE, "w", encoding="utf-8") as f:
            for res in self.reservations:
                f.write(res.to_line())

   # SEAT MANAGEMENT
    # ---- Count booked seats for a specific departure ----
    def count_seats(self, departure, arrival, date, horaire):
        count = 0
        for res in self.reservations:
            t = res.ticket
            if (t.trajet.departure == departure and
                    t.trajet.arrival == arrival and
                    t.date    == date and
                    t.horaire == horaire):
                count += 1
        return count

    # ---- Return True if at least one seat is still available ----
    def is_available(self, departure, arrival, date, horaire):
        return self.count_seats(departure, arrival, date, horaire) < MAX_SEATS

    # ---- Check if ALL time slots are full for a given route and date ----
    def all_slots_full(self, departure, arrival, date):
        return all(
            not self.is_available(departure, arrival, date, h)
            for h in HORAIRES
        )


#=================================================================================#
# ================SADIA'S PART END===================
#=================================================================================#









#=================================================================================#
# ================KABIR'S PART START===================
#=================================================================================#
# ----------------------------------------------------------
# BOOKING STEPS
# Each step guides the user step by step.
# if the user types'b' the step returns none
# and the system automatically returns to the previous step.
# ----------------------------------------------------------
  
#-------Display routes and askthe user to pick one----------
    def _step_choose_route(self):
        print(f"\n{SEPARATOR}")
        print("  BOOK A TICKET  —  Step 1/4: Choose a route")
        print(f"  (type 'b' at any step to go back)")
        print(SEPARATOR)

        for i, trajet in enumerate(TRAJETS, 1):
            print(f"  {i}. {trajet}")

        print(SEPARATOR)
        choice = get_valid_choice(
            "  Select a route (1-6) or 'b' to cancel: ",
            [str(i) for i in range(1, 7)] + [BACK]
        )
        if choice == BACK:
            return None
        return TRAJETS[int(choice) - 1]
#------- Ask the user to enter a travel date----------------
    def _step_choose_date(self):
        print(f"\n{SEPARATOR}")
        print("  BOOK A TICKET  —  Step 2/4: Choose a date")
        print(SEPARATOR)
      while True:
        value = input("  Travel date (DD/MM/YYYY) or 'b' to go back: ").strip()
        if value.lower() == BACK:
            return None
        if validate_date(value):
            return value


#=================================================================================#
# ================KABIR'S PART END===================
#=================================================================================#



#=================================================================================#
# ================ESPERANCE'S PART START===================
#=================================================================================#

# ID GENERATION
#----Generate a unique reservation ID for a given date----
def generate_reservation_id(self, date_str): 
    existing_ids = [r.reservation_id for r in self.reservations]
    counter = len(existing_ids) + 1
    while True:
        new id = generate_id(date_str, counter)
        if new_id not in existing_ids:
            return new_id
        counter += 1
# ----------------------------------------------------------
# MENU OPTION 1 - BOOK A TICKET (step-based with back navigation)
# ----------------------------------------------------------
def book_ticket(self):
    step       = 1
    trajet     = None
    date       = None
    horaire    = None
    first_name = None
    last_name  = None
    phone      = None
    while True:
        # ---- Step 1: Choose route ----
        if step == 1:
            trajet = self._step_choose_route()
            if trajet is None:
               return   # User cancelled → back to main menu
            step = 2
        # ---- Step 2: Choose date ----
        elif step == 2:
            date = self._step_choose_date()
            if date is None:
                step = 1   # Go back to route selection
            else:
                step = 3
        # ---- Step 3: Choose time ----
        elif step == 3:
            horaire = self._step_choose_time(trajet, date)
            if horaire is None:
                step = 2   # Go back to date selection
            else:
                step = 4
        # ---- Step 4: Passenger info ----
        elif step == 4:
            result = self._step_passenger_info()
            if result is None:
                step = 3   # Go back to time selection
            else:
                first_name, last_name, phone = result
                step = 5
                   

           



#=================================================================================#
# ================ESPERANCE'S PART END===================
#=================================================================================#








#=================================================================================#
# ================DIALLO'S PART START===================
#=================================================================================#
 # ----------------------------------------------------------
    # MENU OPTION 2 - VIEW MY RESERVATIONS
    # ----------------------------------------------------------

    # ---- Search and display all reservations linked to a phone number ----
    def view_reservations(self):
        print(f"\n{SEPARATOR}")
        print("  MY RESERVATIONS")
        print(SEPARATOR)

        phone = get_valid_input("  Enter your phone number: ", validate_phone)

        # ---- Filter reservations matching the given phone ----
        results = [r for r in self.reservations if r.phone == phone]

        if not results:
            print("  No reservation found for this phone number.")
            return

        print(f"\n  {len(results)} reservation(s) found:\n")
        for res in results:
            print(res)
            print()
        print(SEPARATOR)

    # ----------------------------------------------------------
    # MENU OPTION 3 - CANCEL A RESERVATION
    # ----------------------------------------------------------

    # ---- Find a reservation by ID and remove it after confirmation ----
    def cancel_reservation(self):
        print(f"\n{SEPARATOR}")
        print("  CANCEL A RESERVATION")
        print(SEPARATOR)

        res_id = get_valid_input(
            "  Enter reservation ID: ", validate_not_empty
        ).upper()

        # ---- Search for the reservation ----
        target = None
        for res in self.reservations:
            if res.reservation_id == res_id:
                target = res
                break

        if not target:
            print(f"  [!] No reservation found with ID: {res_id}")
            return

        # ---- Show reservation details before confirmation ----
        print("\n  Reservation found:")
        print(target)
        print()

        confirm = get_valid_choice(
            "  Are you sure you want to cancel? (y/n): ", ["y", "n"]
        )
        if confirm == "n":
            print("  Cancellation aborted. Your reservation is still active.")
            return

        # ---- Remove and save ----
        self.reservations.remove(target)
        self.save_reservations()
        print(f"\n  [OK] Reservation {res_id} has been successfully cancelled.")



#=================================================================================#
# ================DIALLO'S PART END===================
#=================================================================================#
