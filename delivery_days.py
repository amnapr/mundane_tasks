import json

def get_delivery_days(filename="input.json") -> list:
    """
    Reads a JSON file with weekday delivery flags and returns a list
    of weekdays (mon, tue, ...) where delivery is enabled (value is true).
    """
    try:
        with open(filename, "r") as f:
            delivery_data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"{filename} not found. Please ensure the file exists.")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in {filename}.")

    if not isinstance(delivery_data, dict):
        raise TypeError(f"Expected a dictionary in {filename}, got {type(delivery_data)}")

    valid_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    enabled_days = [day for day in valid_days if delivery_data.get(day, False)]
    rate = delivery_data.get("rate", None)
    no_bottles = delivery_data.get("no_bottles", None)

    return enabled_days,rate,no_bottles
