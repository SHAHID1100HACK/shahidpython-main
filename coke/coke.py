def main():
    amount_due = 50  # total price of Coke
    accepted_coins = [25, 10, 5]  # valid coins

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))

        if coin in accepted_coins:
            amount_due -= coin
        else:
            # Ignore invalid coins
            continue

    change = abs(amount_due)  # if overpaid, return positive change
    print(f"Change Owed: {change}")

main()
