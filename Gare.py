#-----------------------------------------------------------
# ligne 101 a 200
#-----------------------------------------------------------
while True:
            new_id = generate_id(date_str, counter)
            if new_id not in existing_ids:
                return new_id
            counter += 1
# ----------------------------------------------------------
# ETAPES DE RESERVATION
# Chaque étape guide l'utilisateur pas à pas.
# Si l'utilisateur tape 'b', l'étape retourne None
# et le système revient automatiquement à l'étape précédente.
# ----------------------------------------------------------
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

    def _step_choose_date(self):
        print(f"\n{SEPARATOR}")
        print("  BOOK A TICKET  —  Step 2/4: Choose a date")
