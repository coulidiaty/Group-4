# trajet.py - Represents a bus route between two cities

class Trajet:
    """Stores information about a route: departure city, arrival city, and price."""

    def __init__(self, departure, arrival, price):
        # ---- Store route details ----
        self.departure = departure   # Departure city
        self.arrival   = arrival     # Arrival city
        self.price     = price       # Ticket price in FCFA

    #  String representation for display 
    def __str__(self):
        return f"{self.departure} -> {self.arrival} | {self.price} FCFA"

