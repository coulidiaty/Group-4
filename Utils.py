# ============================================================
# utils.py - Reusable helper functions used across the project
# ============================================================

import re
from datetime import datetime

# ---- French month abbreviations (first 2 letters) ----
# Used to build reservation IDs like "25MA001" (May 25)
MONTH_ABBR = {
    1: "JA",  2: "FE",  3: "MR",  4: "AV",
    5: "MA",  6: "JN",  7: "JL",  8: "AO",
    9: "SE", 10: "OC", 11: "NO", 12: "DE"
} #dictionary of year months

def generate_id(date_str, counter):
    """Generate a unique reservation ID from a date string and a counter."""
    day        = date_str[:2]                  # Extract day from "DD/MM/YYYY"
    month_num  = int(date_str[3:5])            # Extract month number
    month_abbr = MONTH_ABBR[month_num]         # Convert to abbreviation
    return f"{day}{month_abbr}{counter:03d}"   # Zero-padded 3-digit counter


def validate_date(date_str: str) -> bool:
    """Validate that the date is in DD/MM/YYYY format and is not in the past."""
    try:
        date = datetime.strptime(date_str, "%d/%m/%Y")
        if date.date() < datetime.today().date():
            print("  [!] The travel date cannot be in the past.")
            return False
        return True
    except ValueError:
        print("  [!] Invalid format. Please use DD/MM/YYYY (e.g. 25/05/2026).")
        return False


def validate_phone(phone: str) -> bool:
    """Validate that the phone number contains 8 to 12 digits only."""
    if re.fullmatch(r'\d{8,12}', phone):
        return True
    print("  [!] Invalid phone number. Enter 8 to 12 digits only.")
    return False


def validate_not_empty(value: str) -> bool:
    """Validate that the input field is not empty."""
    if value.strip():
        return True
    print("  [!] This field cannot be empty.")
    return False


def get_valid_input(prompt, validator=None):
    """Prompt the user until valid input is received."""
    while True:
        value = input(prompt).strip()
        if validator is None or validator(value):
            return value


def get_valid_choice(prompt, valid_choices):
    """Prompt the user to choose from a fixed set of valid options."""
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print(f"  [!] Please enter one of the following: {', '.join(valid_choices)}")