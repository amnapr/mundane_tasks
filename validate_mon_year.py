import sys
from custom_exception import DateTimeException

def validate_month(month):
    """Validate that month is an integer between 1 and 12."""
    try:
        month = int(month)
    except (TypeError, ValueError) as e:
        raise DateTimeException(f"Invalid month input: {e}")
    
    if 1 <= month <= 12:
        return month
    
    raise DateTimeException(f"Month should be between 1 and 12, not {month}")


def validate_year(year):
    """Validate that year is an integer, either 2024 or 2050."""
    try:
        year = int(year)
    except (TypeError, ValueError) as e:
        raise DateTimeException(f"Invalid year input: {e}")
    
    if year not in range(2024, 2051):
        raise DateTimeException("This program supports only years 2024 and 2050.")
    
    return year


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <month> <year>")
        sys.exit(1)

    mon_input, yr_input = sys.argv[1:3]

    try:
        mon = validate_month(mon_input)
        yr = validate_year(yr_input)
        print(f"{mon=}, {yr=}")
    except DateTimeException as e:
        print(f"Validation failed: {e}")
        sys.exit(2)


if __name__ == "__main__":
    main()