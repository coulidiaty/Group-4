--------------------Ticket Nana - Bus Reservation System---------------------

Ticket Nana is a command-line application built in Python that allows users to book, view, and cancel bus tickets between three cities in Burkina Faso which are Ouagadougou, Koudougou, and Bobo-Dioulasso. All reservations are saved in a local text file so data is not lost when the program closes.

-------------How to Run the Project------------------------------------------

Requirements: Python 3.x (no external libraries needed)

Steps:
Clone the repository: on your terminal (powershell) type git clone https://github.com/coulidiaty/Group-4.git

Go into the project folder: cd Group-4
Run the application: python main.py

--------------------------------Features-------------------------------------

Book a bus ticket step by step (route, date, time, passenger info)
View all reservations linked to a phone number
Cancel a reservation using its unique ID
Navigate back at any step by typing b
Real-time seat availability per time slot
Reservations saved automatically to a text file

----------------------------Technologies Used--------------------------------

Language: Python 3.x
Libraries: os, re, datetime (all built-in, no installation needed)

---------------------------Project Structure---------------------------------
Group-4/
--- main.py # Entry point --- displays the menu and starts the app
--- gare.py # Core business logic --- booking, viewing, cancelling
--- reservation.py # Reservation class --- groups passenger and ticket data
--- ticket.py # Ticket classes --- Ticket (parent) and TicketStandard (child)
--- trajet.py # Trajet class --- represents a route between two cities
--- utils.py # Helper functions --- input validation and ID generation
--- reservations.txt # Auto-generated file where reservations are stored

-----------------------------OOP Structure (POO)-------------------------------
Trajet --- trajet.py
Represents a bus route between two cities.

Attributes: departure, arrival, price
Methods: **str**

Ticket --- ticket.py
Base class for all ticket types.

Attributes: trajet, date, horaire
Methods: get_info

TicketStandard --- ticket.py
Inherits from Ticket. Represents a standard economy ticket.

Additional attribute: type = "Standard"
Methods: get_info (overrides parent)

Reservation --- reservation.py
Groups all data for a single booking.

Attributes: reservation_id, first_name, last_name, phone, ticket
Methods: to_line (serialize to text file), **str**

GareRoutiere --- gare.py
Main class of the application. Handles all user-facing operations.

Attributes: reservations
Methods:

load_reservations --- reads and rebuilds reservations from file
save_reservations --- writes all reservations back to file
count_seats --- counts booked seats for a given departure
is_available --- checks if seats are available
all_slots_full --- checks if all time slots are full
generate_reservation_id --- generates a unique ID per reservation
\_step_choose_route --- step 1 of booking
\_step_choose_date --- step 2 of booking
\_step_choose_time --- step 3 of booking
\_step_passenger_info --- step 4 of booking
\_step_confirm --- confirmation screen
book_ticket --- runs the full booking flow
view_reservations --- displays reservations by phone number
cancel_reservation --- cancels a reservation by ID

------------------------------- Acknowledgements-----------------------------

.Python official documentation: https://docs.python.org
. Git & GitHub documentation: https://docs.github.com
.datetime module reference: https://docs.python.org/3/library/datetime.html
.re module reference: https://docs.python.org/3/library/re.html
.youtube videos: https://youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&si=fP-0hYF0M5EX58ZC , https://youtube.com/playlist?list=PL0lo9MOBetEFcp4SCWinBdpml9B2U25-f&si=0nX-z54LzLCc6nwM ,
.Debbuging and better syntax : Claude IA
.Our lecturer: Miss Kweyakie Afi Blebo

-----------------------------------Team Members--------------------------------

- Dera Alimatou Sadia --- https://github.com/DeraAlimatouSadia
- Diallo Maïmounata --- https://github.com/diallomaimounata51-byte
- Diallo Aïssata --- https://github.com/princess-19
- Guissou Abdoul Kabir --- https://github.com/kabir-0009
- KIEMA Espérance Wendkuni 1ere jumelle ---https://github.com/kiemaesperance
- Zaïd Diataga Coulidiaty --- https://github.com/coulidiaty
