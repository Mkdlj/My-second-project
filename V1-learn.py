"""
Data Representation Utility
--------------------------
A simple Python script to demonstrate conversions between 
Decimal, ASCII, and Binary formats.
"""

def main():
    # --- Decimal to Binary Conversion ---
    # Initialize a base-10 integer
    decimal_val = 43
    # Convert to binary string
    binary_val = bin(decimal_val)
    
    print(f"[Decimal] {decimal_val}  =>  [Binary] {binary_val}")

    # --- ASCII to Binary Conversion ---
    # Define input character
    char_input = "A"
    # Get Unicode/ASCII integer value
    ascii_code = ord(char_input)
    # Convert integer to binary
    char_binary = bin(ascii_code)

    print(f"[Char] '{char_input}'  =>  [ASCII] {ascii_code}  =>  [Binary] {char_binary}")

if __name__ == "__main__":
    main()