import sys
from delivery_days import get_delivery_days
from mon_distribution import calendar_distribution
from validate_mon_year import validate_month, validate_year



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <month> <year>")
        sys.exit(1)

    mon_input, yr_input = sys.argv[1:3]
    mon_input.strip()
    yr_input.strip()

    if mon_input.isdigit() and yr_input.isdigit():
        mon = int(mon_input) if validate_month(mon_input) else None
        yr = int(yr_input) if validate_year(yr_input) else None
        day_dist = calendar_distribution(yr,mon)
        print(day_dist)
        delivery_days,rate,no_bottles = get_delivery_days()
        total = sum(day_dist[day] for day in delivery_days if day in day_dist)
        print(f'Total delivery days: {total} in {mon_input} {yr_input}')
        # print(delivery_days)
        total_cost = no_bottles * rate * total
        print(f'Total cost: {total_cost}')
        
    else:
        raise TypeError(f'Input should be in MM YYYY format')


    
