# ============================================================
# reservation.py - Groups all data for a single booking
# ============================================================

class Reservation:
    """
    Holds all information related to one reservation:
    ID, passenger details, and the associated ticket.
    """

    def __init__(self, reservation_id, first_name, last_name, phone, ticket):
        # ---- Reservation identity ----
        self.reservation_id = reservation_id   # this ID  is unique for each ticket(e.g. "25MA001")

        # ---- Passenger information ----
        self.first_name = first_name
        self.last_name  = last_name
        self.phone      = phone

        # ---- Ticket attached to this reservation ----
        self.ticket = ticket   # TicketStandard object

    # ---- Serialize reservation to a single line for file storage ----
    #  Ticket Format: id|first-name|last-name|phone|departure|arrival|price|date|time
    def to_line(self):
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

    # ---- For reservation ----
    def __str__(self):
        t = self.ticket
        return (
            f"  ID: {self.reservation_id} | "
            f"{t.trajet.departure} -> {t.trajet.arrival} | "
            f"Date: {t.date} | "
            f"Time: {t.horaire} | "
            f"Price: {t.trajet.price} FCFA | "
            f"Passenger: {self.first_name} {self.last_name}"
        )
