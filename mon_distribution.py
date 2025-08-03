from collections import defaultdict
from calendar import monthcalendar, day_name

def calendar_distribution(year: int, month: int) -> dict:
    """
    Returns a distribution of how many times each weekday occurs in the given month and year.
    """
    day_distribution = defaultdict(int)

    for week in monthcalendar(year, month):
        for index, day_number in enumerate(week):
            if day_number != 0:
                weekday = day_name[index].lower()[:3]
                day_distribution[weekday] += 1

    return dict(day_distribution)

if __name__ == "__main__":
    year, month = input("Enter Month and Date in MM YYYY:").split()
    print(calendar_distribution(int(month), int(year)))