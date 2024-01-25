import sys

def Calculate_range_automobile(battery_level):
    try:
        if not battery_level.isdigit():
            raise ValueError("Invalid character in battery level")

        battery_level = int(battery_level)

        if not (0 <= battery_level <= 100):
            raise ValueError("Invalid number: must be an integer between 0 and 100")

        result=(((battery_level / 100) * 62) / 15.6) * 100
        return f"{result:.0f} km"
    except ValueError as e:
        print(f"Error in function 'Calculate_range_automobile': {e}")
        return None

def main():
    try:
        if len(sys.argv) == 2:
            for arg in sys.argv[1:]:
                result = Calculate_range_automobile(arg)
                if result is not None:
                    print(result)
        else:
            raise ValueError("Invalid number of arguments!")
    except ValueError as e:
        print(f"Error in main: {e}")

if __name__ == '__main__':
    main()
