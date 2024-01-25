import sys
def Valid_ID_RO(func):
    def wrapper(id_ro):
        try:
            if len(id_ro) != 10:
                raise ValueError(f"Invalid length for id={id_ro}")
            if not id_ro.isdigit():
                raise ValueError(f"Invalid character or id={id_ro}")

            return func(id_ro)
        except ValueError as e:
            print(f"Error in function '{func.__name__}': {e}")
            return None

    return wrapper

@Valid_ID_RO
def Print_birthday_id_ro(id_ro):
    print(id_ro[1:3])

def main():
    try:
        if len(sys.argv) > 1:
            for arg in sys.argv[1:]:
                Print_birthday_id_ro(arg)
        else:
            raise ValueError("Need at least 1 argument!")
    except ValueError as e:
        print(f"Error in main: {e}")

if __name__ == '__main__':
    main()
