# ============================================================
# trajet.py - Represents a bus route between two cities
# ============================================================

class Trajet:
    """Stores information about a route: departure city, arrival city, and price."""

    def __init__(self, departure, arrival, price):
        """Initialize a route with departure city, arrival city, and ticket price."""
        # ---- Store route details ----
        self.departure = departure   # Departure city
        self.arrival   = arrival     # Arrival city
        self.price = float(price)    # Ticket price in FCFA

    def __str__(self):
        """Return a formatted string representation of the route."""
        return f"{self.departure} -> {self.arrival} | {self.price} FCFA"
