def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Rule 1: Length must be between 2 and 6
    if not (2 <= len(s) <= 6):
        return False

    # Rule 2: Must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Rule 3: Only letters and numbers allowed
    if not s.isalnum():
        return False

    # Rule 4: Numbers must be at the end, and no leading 0
    number_started = False
    for i in range(len(s)):
        if s[i].isdigit():
            if not number_started:
                # First digit shouldn't be '0'
                if s[i] == '0':
                    return False
                number_started = True
        elif number_started:
            # If letter comes after number → invalid
            return False

    return True

main()
