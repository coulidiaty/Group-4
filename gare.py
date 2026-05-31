# ============================================================
# gare.py - GareRoutiere class: core business logic
# Handles all operations: loading, booking, viewing, cancelling
# ============================================================

import os
from trajet      import Trajet
from ticket      import TicketStandard
from reservation import Reservation
from utils       import (generate_id, validate_date, validate_phone,
                         validate_not_empty, get_valid_input, get_valid_choice)

# ---- Application constants ----
RESERVATIONS_FILE = "reservations.txt"
MAX_SEATS         = 30
HORAIRES          = ("06:00", "13:00", "20:00")   # tuple of available departure times

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
        """Initialize the application and load existing reservations from file."""
        self.reservations = self.load_reservations()

    # ----------------------------------------------------------
    # FILE OPERATIONS
    # ----------------------------------------------------------

    def load_reservations(self):
        """Read reservations.txt and rebuild the reservations list."""
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

    def save_reservations(self):
        """Write all current reservations back to the file."""
        with open(RESERVATIONS_FILE, "w", encoding="utf-8") as f:
            for res in self.reservations:
                f.write(res.to_line())

    # ----------------------------------------------------------
    # SEAT MANAGEMENT
    # ----------------------------------------------------------

    def count_seats(self, departure, arrival, date, horaire):
        """Count the number of booked seats for a specific route, date and time."""
        count = 0
        for res in self.reservations:
            t = res.ticket
            if (t.trajet.departure == departure and
                    t.trajet.arrival == arrival and
                    t.date    == date and
                    t.horaire == horaire):
                count += 1
        return count

    def is_available(self, departure, arrival, date, horaire):
        """Return True if at least one seat is still available for the given slot."""
        return self.count_seats(departure, arrival, date, horaire) < MAX_SEATS

    def all_slots_full(self, departure, arrival, date):
        """Return True if all time slots are fully booked for a given route and date."""
        return all(
            not self.is_available(departure, arrival, date, h)
            for h in HORAIRES
        )

    # ----------------------------------------------------------
    # ID GENERATION
    # ----------------------------------------------------------

    def generate_reservation_id(self, date_str):
        """Generate a unique reservation ID for a given travel date."""
        existing_ids = [r.reservation_id for r in self.reservations]
        counter = len(existing_ids) + 1
        while True:
            new_id = generate_id(date_str, counter)
            if new_id not in existing_ids:
                return new_id
            counter += 1

    # ----------------------------------------------------------
    # BOOKING STEPS (each returns None if user pressed 'b')
    # ----------------------------------------------------------

    def _step_choose_route(self):
        """Display available routes and ask the user to pick one. Returns Trajet or None."""
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

    def _step_choose_date(self):
        """Ask the user to enter a valid travel date. Returns date string or None."""
        print(f"\n{SEPARATOR}")
        print("  BOOK A TICKET  —  Step 2/4: Choose a date")
        print(SEPARATOR)

        while True:
            value = input("  Travel date (DD/MM/YYYY) or 'b' to go back: ").strip()
            if value.lower() == BACK:
                return None
            if validate_date(value):
                return value

    def _step_choose_time(self, trajet, date):
        """Show available time slots and ask the user to pick one. Returns horaire or None."""
        print(f"\n{SEPARATOR}")
        print("  BOOK A TICKET  —  Step 3/4: Choose a departure time")
        print(SEPARATOR)

        # ---- Warn immediately if the entire route+date is fully booked ----
        if self.all_slots_full(trajet.departure, trajet.arrival, date):
            print(f"  [!] All time slots for {trajet.departure} -> {trajet.arrival}")
            print(f"      on {date} are fully booked. Please choose another date.")
            return None

        # ---- Display each time slot with remaining seats ----
        for i, h in enumerate(HORAIRES, 1):
            seats_left = MAX_SEATS - self.count_seats(
                trajet.departure, trajet.arrival, date, h
            )
            if seats_left > 0:
                status = f"{seats_left} seat(s) available"
            else:
                status = "FULL"
            print(f"  {i}. {h}  —  {status}")

        print(SEPARATOR)
        choice = get_valid_choice(
            "  Select a time (1-3) or 'b' to go back: ",
            ["1", "2", "3", BACK]
        )
        if choice == BACK:
            return None

        horaire = HORAIRES[int(choice) - 1]

        # ---- Double-check the chosen slot is not full ----
        if not self.is_available(trajet.departure, trajet.arrival, date, horaire):
            print("  [!] This slot is fully booked. Please choose another time.")
            return self._step_choose_time(trajet, date)

        return horaire

    def _step_passenger_info(self):
        """Collect passenger first name, last name and phone. Returns tuple or None."""
        print(f"\n{SEPARATOR}")
        print("  BOOK A TICKET  —  Step 4/4: Passenger information")
        print(f"  (type 'b' in the first field to go back)")
        print(SEPARATOR)

        # ---- First name: allow 'b' to go back ----
        first_name = input("  First name  : ").strip()
        if first_name.lower() == BACK:
            return None

        # ---- Validate first name is not empty ----
        while not validate_not_empty(first_name):
            first_name = input("  First name  : ").strip()

        # ---- Last name and phone: no back from here, validate only ----
        while True:
            last_name = input("  Last name   : ").strip()
            if validate_not_empty(last_name):
                break

        while True:
            phone = input("  Phone number: ").strip()
            if validate_phone(phone):
                break

        return first_name.capitalize(), last_name.upper(), phone

    def _step_confirm(self, trajet, date, horaire, first_name, last_name, phone):
        """Show booking summary and ask for confirmation. Returns True, False, or None."""
        print(f"\n{SEPARATOR}")
        print("  BOOKING SUMMARY — Please review before confirming")
        print(SEPARATOR)
        print(f"  {'Route':<12}: {trajet.departure} -> {trajet.arrival}")
        print(f"  {'Date':<12}: {date}")
        print(f"  {'Time':<12}: {horaire}")
        print(f"  {'Price':<12}: {trajet.price} FCFA")
        print(f"  {'Passenger':<12}: {first_name} {last_name}")
        print(f"  {'Phone':<12}: {phone}")
        print(f"  {'Ticket type':<12}: Standard")
        print(SEPARATOR)

        choice = get_valid_choice(
            "  Confirm booking? (y / n / b to edit): ",
            ["y", "n", BACK]
        )
        if choice == BACK:
            return None
        if choice == "n":
            return False
        return True

    # ----------------------------------------------------------
    # MENU OPTION 1 - BOOK A TICKET (step-based with back navigation)
    # ----------------------------------------------------------

    def book_ticket(self):
        """Run the full ticket booking flow with step-by-step navigation."""
        step       = 1
        trajet     = None
        date       = None
        horaire    = None
        first_name = None
        last_name  = None
        phone      = None

        while True:

            if step == 1:
                trajet = self._step_choose_route()
                if trajet is None:
                    return
                step = 2

            elif step == 2:
                date = self._step_choose_date()
                if date is None:
                    step = 1
                else:
                    step = 3

            elif step == 3:
                horaire = self._step_choose_time(trajet, date)
                if horaire is None:
                    step = 2
                else:
                    step = 4

            elif step == 4:
                result = self._step_passenger_info()
                if result is None:
                    step = 3
                else:
                    first_name, last_name, phone = result
                    step = 5

            elif step == 5:
                result = self._step_confirm(
                    trajet, date, horaire, first_name, last_name, phone
                )
                if result is None:
                    step = 4
                elif result is False:
                    print("  Booking cancelled. No reservation was made.")
                    return
                else:
                    res_id      = self.generate_reservation_id(date)
                    ticket      = TicketStandard(trajet, date, horaire)
                    reservation = Reservation(
                        res_id, first_name, last_name, phone, ticket
                    )
                    self.reservations.append(reservation)
                    self.save_reservations()

                    print(f"\n  [OK] Booking confirmed!")
                    print(f"  Your reservation ID : {res_id}")
                    print(f"  Keep this ID to cancel your reservation if needed.")
                    return

    # ----------------------------------------------------------
    # MENU OPTION 2 - VIEW MY RESERVATIONS
    # ----------------------------------------------------------

    def view_reservations(self):
        """Search and display all reservations linked to a phone number."""
        print(f"\n{SEPARATOR}")
        print("  MY RESERVATIONS")
        print(SEPARATOR)

        phone = get_valid_input("  Enter your phone number: ", validate_phone)

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

    def cancel_reservation(self):
        """Find a reservation by ID and remove it after user confirmation."""
        print(f"\n{SEPARATOR}")
        print("  CANCEL A RESERVATION")
        print(SEPARATOR)

        res_id = get_valid_input(
            "  Enter reservation ID: ", validate_not_empty
        ).upper()

        target = None
        for res in self.reservations:
            if res.reservation_id == res_id:
                target = res
                break

        if not target:
            print(f"  [!] No reservation found with ID: {res_id}")
            return

        print("\n  Reservation found:")
        print(target)
        print()

        confirm = get_valid_choice(
            "  Are you sure you want to cancel? (y/n): ", ["y", "n"]
        )
        if confirm == "n":
            print("  Cancellation aborted. Your reservation is still active.")
            return

        self.reservations.remove(target)
        self.save_reservations()
        print(f"\n  [OK] Reservation {res_id} has been successfully cancelled.")
