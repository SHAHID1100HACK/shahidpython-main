import sys
import pyfiglet

# Get all available fonts
available_fonts = pyfiglet.FigletFont.getFonts()

# Check arguments
if len(sys.argv) == 1:
    # No font specified, use random
    figlet = pyfiglet.Figlet()
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in available_fonts:
    # Specific font provided
    figlet = pyfiglet.Figlet(font=sys.argv[2])
else:
    # Invalid usage
    sys.exit("Invalid usage")

# Get user input
text = input("Input: ")

# Output in the selected font
print("Output:")
print(figlet.renderText(text))
