import json

def get_delivery_schedule() -> dict:
    """
    Prompts user for days when delivery is not needed and returns a dictionary
    of weekdays with boolean delivery flags.
    """
    valid_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    delivery_flags = {day: True for day in valid_days}

    user_input = input(
        "Enter the day(s) when delivery is NOT needed (e.g. sun, mon,tue). "
        "Enter 'none' if delivery is needed every day:\n> "
    ).strip().lower()

    if user_input != "none" and user_input != "":
        days_off = [d.strip() for d in user_input.split(",") if d.strip()]
        for day in days_off:
            if day in valid_days:
                delivery_flags[day] = False
            else:
                print(f"[Warning] Ignored invalid day: {day}")

    return delivery_flags


def get_order_config() -> dict:
    """
    Prompts the user for the number of bottles and rate.
    """
    while True:
        try:
            no_bottles = int(input("Enter number of bottles:\n> "))
            rate = float(input("Enter rate per bottle:\n> "))
            return {"no_bottles": no_bottles, "rate": rate}
        except ValueError:
            print("[Error] Please enter valid numeric values.")


def write_json(filename: str, data: dict):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"[Success] Config written to: {filename}")


def main():
    delivery_flags = get_delivery_schedule()
    order_config = get_order_config()

    combined_config = {**order_config, **delivery_flags}
    write_json("input.json", combined_config)


if __name__ == "__main__":
    main()
