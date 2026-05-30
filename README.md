Group-4 - Ticket Nana Bus Reservation System

Description
This is a bus reservation system made in python for school project.
the user can book tickets, see their reservations and cancel them.
the available cities are Ouagadougou Koudougou and Bobo-Dioulasso
How to run the project
you need python 3 installed on you computer
clone the project :
git clone https://github.com/coulidiaty/Group-4.git
then run :
python main.py by opening the file with python

Fonctionnalites
book a ticket
see reservations
cancel a reservation
the user can go back by typing b

Technologies used
python 3
os, re, datetime (which are already included in python)

project structure
main.py : start the app and show the menu
gare.py : the main logic of the app (booking viewing cancelling)
reservation.py : reservation class
ticket.py : ticket class and ticketstandard class
trajet.py : trajet class for the routes
utils.py : helper functions for validation and id generation
reservations.txt : where reservations are saved

POO structure
Trajet
represents a route
attributes : departure arrival price
Ticket
base class for tickets
attributes : trajet date horaire
methods : get_info
TicketStandard
inherits from ticket
adds type = standard
Reservation
groups all data for one booking
attributes : reservation_id first_name last_name phone ticket
methods : to_line, str
GareRoutiere
main class
handles everything
methods : load_reservations, save_reservations, book_ticket, view_reservations, cancel_reservation and more

Acknowledgments
python docs
github docs
our teacher
