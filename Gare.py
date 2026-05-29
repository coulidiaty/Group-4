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
# ID GENERATION
#===================================
#=====Generate a unique reservation ID for a given date===
def generate_reservation_id(self, date_str): 
    existing_ids = [r.reservation_id for r in self.reservations]
    counter = len(existing_ids) + 1
    while True:
        new id = generate_id(date_str, counter)
        if new_id not in existing_ids:
            return new_id
        counter += 1



#=================================================================================#
# ================ESPERANCE'S PART END===================
#=================================================================================#








#=================================================================================#
# ================DIALLO'S PART START===================
#=================================================================================#



#=================================================================================#
# ================DIALLO'S PART END===================
#=================================================================================#
