def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            if y == 0 or x > y:
                raise ValueError

            percent = round((x / y) * 100)

            if percent <= 1:
                print("E")
            elif percent >= 99:
                print("F")
            else:
                print(f"{percent}%")
            break

        except (ValueError, ZeroDivisionError):
            # If input is invalid (not numbers, x > y, or y is 0), try again
            pass

main()
