# --- Part 1: Decimal to Binary Conversion ---

# Define an integer in base 10 (Decimal)
decimal_number = 43

# Convert the decimal integer to a binary string using the built-in bin() function
# Note: The '0b' prefix in the output indicates a binary literal
binary_number = bin(decimal_number)

# Output the result using an f-string
print(f"{decimal_number} in binary is {binary_number}")


# --- Part 2: Character to ASCII and Binary ---

# Define a single character variable
char = "A"

# Use ord() to get the integer representing the Unicode/ASCII code point of the character
ascii_number = ord(char)

# Convert that ASCII integer value into its binary representation
binary_of_char = bin(ascii_number)

# Display the full conversion path: Character -> ASCII Code -> Binary
print(f"Character {char} -> ASCII {ascii_number} -> Binary {binary_of_char}")