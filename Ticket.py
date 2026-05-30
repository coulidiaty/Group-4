class Ticket:
    """Base class for all ticket types. Stores route, date, and departure time."""

    def __init__(self, trajet, date, horaire):
        """Initialize a ticket with a route, travel date, and departure time."""
        self.trajet  = trajet
        self.date    = date
        self.horaire = horaire

    def get_info(self):
        """Return basic ticket information as a formatted string."""
        return f"{self.trajet} | {self.date} | {self.horaire}"


class TicketStandard(Ticket):
    """Standard economy ticket. Inherits all fields from Ticket."""

    def __init__(self, trajet, date, horaire):
        """Initialize a standard ticket and set its type label."""
        super().__init__(trajet, date, horaire)
        self.type = "Standard"

    def get_info(self):
        """Return full ticket info including the ticket type."""
        return f"[{self.type}] {super().get_info()}"