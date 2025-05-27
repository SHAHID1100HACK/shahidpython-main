def main():
    prompt = input("Enter: ").strip()
    snake = ""

    for char in prompt:
        if char.isupper():
            snake += "_" + char.lower()  # add underscore and lowercase version
        else:
            snake += char  # keep the character as is

    print(snake)

main()
