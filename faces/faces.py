# replaces the emioti text too real emoji
def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    #  input
    user_input = input("Enter: ")
    # Convert emoticons and print the result
    print(convert(user_input))

# al last
main()
