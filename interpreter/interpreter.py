# interpreter.py

# 🟩 Function Definition
def main():
    # 🟨 INPUT FUNCTION
    # This asks the user to type something.
    # Whatever the user types is stored as a string in `expression`.
    expression = input("Expression: ")

    # 🟦 STRING SPLITTING
    # .split() breaks the string by spaces into three parts:
    # For example: "3 + 4" becomes ["3", "+", "4"]
    x, operator, z = expression.split()

    # 🟥 TYPE CONVERSION
    # Converts string "3" and "4" to actual numbers (integers).
    x = int(x)
    z = int(z)

    # 🟪 IF-ELIF CONDITIONS
    # This checks what kind of math operation the user wants.
    # It compares the operator and does the matching operation.
    if operator == "+":
        result = x + z
    elif operator == "-":
        result = x - z
    elif operator == "*":
        result = x * z
    elif operator == "/":
        result = x / z  # No need to check for divide by zero since we assume z ≠ 0

    # 🟫 FORMATTED OUTPUT
    # This prints the answer rounded to 1 decimal place.
    # For example: 5 becomes 5.0, 7.25 stays 7.2
    print(f"{result:.1f}")

# 🟧 FUNCTION CALL
# This runs the main() function to start the program
main()
