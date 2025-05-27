import emoji

# Get user input
text = input("Input: ")

# Convert codes to emoji
converted = emoji.emojize(text, language="alias")

# Output the result
print(f"Output: {converted}")
