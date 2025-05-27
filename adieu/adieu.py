import sys

names = []

try:
    while True:
        name = input("Name: ")
        names.append(name)
except EOFError:
    print()  # for clean newline

if len(names) == 1:
    message = names[0]
elif len(names) == 2:
    message = f"{names[0]} and {names[1]}"
else:
    message = ", ".join(names[:-1]) + f", and {names[-1]}"

print(f"Adieu, adieu, to {message}")
