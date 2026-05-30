# ============================================================
# reservation.py - Groups all data for a single booking
# ============================================================

class Reservation:
    """
    Holds all information related to one reservation:
    ID, passenger details, and the associated ticket.
    """

    def __init__(self, reservation_id, first_name, last_name, phone, ticket):
        """Initialize a reservation with a unique ID, passenger info, and a ticket."""
        # ---- Reservation identity ----
        self.reservation_id = reservation_id   # Unique ID (e.g. "25MA001")

        # ---- Passenger information ----
        self.first_name = first_name
        self.last_name  = last_name
        self.phone      = phone

        # ---- Ticket attached to this reservation ----
        self.ticket = ticket   # TicketStandard object

    def to_line(self):
        """Serialize the reservation to a single pipe-separated line for file storage."""
        t = self.ticket
        return (
            f"{self.reservation_id}|"
            f"{self.first_name}|"
            f"{self.last_name}|"
            f"{self.phone}|"
            f"{t.trajet.departure}|"
            f"{t.trajet.arrival}|"
            f"{t.trajet.price}|"
            f"{t.date}|"
            f"{t.horaire}\n"
        )

    def __str__(self):
        """Return a human-readable summary of the reservation."""
        t = self.ticket
        return (
            f"  ID: {self.reservation_id} | "
            f"{t.trajet.departure} -> {t.trajet.arrival} | "
            f"Date: {t.date} | "
            f"Time: {t.horaire} | "
            f"Price: {t.trajet.price} FCFA | "
            f"Passenger: {self.first_name} {self.last_name}"
        )