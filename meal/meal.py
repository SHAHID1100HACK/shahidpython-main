def main():
    time = input("What time is it? ").strip()
    hour = convert(time)

    if 7 <= hour <= 8:
        print("breakfast time")
    elif 12 <= hour <= 13:
        print("lunch time")
    elif 18 <= hour <= 19:
        print("dinner time")

def convert(time):
    h, m = time.split(":")
    h = int(h)
    m = int(m)
    return h + m / 60

if __name__ == "__main__":
    main()
