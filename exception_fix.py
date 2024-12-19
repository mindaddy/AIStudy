def main():
    try:
        divisor = 0
        x = 1 / divisor
    except ZeroDivisionError as e:
        print("ZeroDivisionError:", e)
    
    try:
        my_dict = {'name': 'Alice'}
        age = my_dict['age']
    except KeyError as e:
        print("KeyError:", e)

    try:
        int('abc')  # ValueError
    except ValueError as e:
        print("ValueError:", e)

if __name__ == "__main__":
    main()
