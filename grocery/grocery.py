def main():
    grocery_list = {}

    while True:
        try:
            # Ask for item and normalize input to uppercase
            item = input().strip().upper()

            # Count how many times each item is entered
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except EOFError:
            print()  # For clean exit on Ctrl+D
            break

    # Print grocery list sorted alphabetically
    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item}")

main()
