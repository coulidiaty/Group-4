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
}


# ---- Generate a unique reservation ID ----
# Format: day (2 digits) + month abbreviation (2 letters) + counter (3 digits)
# Example: "25MA001" for the 1st reservation on May 25
def generate_id(date_str, counter):
    day        = date_str[:2]                  # Extract day from "DD/MM/YYYY"
    month_num  = int(date_str[3:5])            # Extract month number
    month_abbr = MONTH_ABBR[month_num]         # Convert to abbreviation
    return f"{day}{month_abbr}{counter:03d}"   # Zero-padded 3-digit counter
# ---- Validate a date entered by the user ----
# Accepts DD/MM/YYYY format only; rejects past dates
def validate_date(date_str):
    try:
        date = datetime.strptime(date_str, "%d/%m/%Y")
        if date.date() < datetime.today().date():
            print("  [!] The travel date cannot be in the past.")
            return False
        return True
    except ValueError:
        print("  [!] Invalid format. Please use DD/MM/YYYY (e.g. 25/05/2026).")
        return False


# ---- Validate a phone number ----
# Accepts 8 to 12 consecutive digits (no spaces or symbols)
def validate_phone(phone):
    if re.fullmatch(r'\d{8,12}', phone):
        return True
    print("  [!] Invalid phone number. Enter 8 to 12 digits only.")
    return False


# ---- Validate that a text field is not empty ----
def validate_not_empty(value):
    if value.strip():
        return True
    print("  [!] This field cannot be empty.")
    return False


# ---- Prompt the user until valid input is received ----
# Accepts an optional validator function; loops until it returns True
def get_valid_input(prompt, validator=None):
    while True:
        value = input(prompt).strip()
        if validator is None or validator(value):
            return value


# ---- Prompt the user to choose from a fixed set of options ----
# Loops until a valid option is entered
def get_valid_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print(f"  [!] Please enter one of the following: {', '.join(valid_choices)}")
