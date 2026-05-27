
class Ticket:
   

    def __init__(self, trajet, date, horaire):
        self.trajet  = trajet    # Trajet object (route + price)
        self.date    = date      # Travel date as string (DD/MM/YYYY)
        self.horaire = horaire   # Departure time (e.g. "06:00")

    def get_info(self):
        return f"{self.trajet} | {self.date} | {self.horaire}"



class TicketStandard(Ticket):
  

    def __init__(self, trajet, date, horaire):
        # Call parent constructor to initialize shared fields
        super().__init__(trajet, date, horaire)
        self.type = "Standard"   # Ticket category label

    def get_info(self):
        return f"[{self.type}] {super().get_info()}"
