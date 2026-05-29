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
