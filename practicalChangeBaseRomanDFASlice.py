# Helper function to convert integers to Roman numerals
def to_roman(n):
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    roman = ''
    for value, numeral in roman_numerals:
        while n >= value:
            roman += numeral
            n -= value
    return roman

# Helper function to convert a character to its decimal value
def char_to_value(c):
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    elif 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 10
    return ("Invalid character in input string")

# Helper function to convert a decimal value to its character equivalent
def value_to_char(v, base):
    if v < 36:
        if 0 <= v <= 9:
            return chr(v + ord('0'))
        elif 10 <= v <= 35:
            return chr(v - 10 + ord('A'))
    # For base 37, values 36 and above should be Roman numerals
    elif base == 37 and v >= 36:
        return to_roman(v - 35)  # Start Roman numerals at 36
    return ("Invalid value")

# Function to convert a number from one base to another
def base_conversion(input_string, current_base, required_base):
    # Step 1: Convert from the current base to base 10
    input_string = input_string.upper()
    base_10 = 0
    for char in input_string:
        base_10 = base_10 * current_base + char_to_value(char)

    # Step 2: Convert from base 10 to the required base (including base 37)
    if base_10 == 0:
        return '0'

    output_string = ''
    while base_10 > 0:
        remainder = base_10 % required_base
        output_string = value_to_char(remainder, required_base) + output_string
        base_10 //= required_base

    return output_string

# Example usage:
input_string = "1010"  # binary input
current_base = 2       # base 2 (binary)
required_base = 37     # base 37 (with Roman numerals)

output = base_conversion(input_string, current_base, required_base)
print(output)  # Should print "A" for the binary "1010" (which is 10 in decimal) in base 37


# slice opertator
def custom_slice(sequence, start=None, stop=None, step=1):
    # Handle sequence length
    length = len(sequence)

    # If step is zero, raise an error (as Python does with slices)
    if step == 0:
       return ("Step cannot be zero")

    # Handle None values for start and stop, mimicking default slice behavior
    if start is None:
        start = 0 if step > 0 else length - 1
    if stop is None:
        stop = length if step > 0 else -1

    # Normalize negative indices
    if start < 0:
        start += length
    if stop < 0:
        stop += length

    # Cap start and stop values within valid index range (like slice operator)
    start = max(0, min(length, start))
    stop = max(0, min(length, stop))

    # Create an empty list to store the result (works for both lists and strings)
    result = []

    # Iterate through the sequence manually based on start, stop, and step
    i = start
    while (step > 0 and i < stop) or (step < 0 and i > stop):
        result.append(sequence[i])
        i += step

    # Return as string if the input is a string, otherwise return list
    return ''.join(result) if isinstance(sequence, str) else result

# Example usage with list:
lst = [0, 1, 2, 3, 4, 5, 6]
print(custom_slice(lst, 1, 10, 2))  # Output: [1, 3, 5]

# Example usage with string:
s = "Hello, World!"
print(custom_slice(s, -4, 100))  # Output: 'Hello, World!'


# dfa function

# Define the alphabet for valid symbols
alphabet = {'a', 'b'}

def q0(text):
    # If the input string is empty, return the current state
    if text == '':
        return 'q0'
    
    symbol = text[0]
    
    # Check if the symbol is in the alphabet
    if symbol in alphabet:
        if symbol == 'a':
            return q1(text[1:])  # Move to q1 if the symbol is 'a'
        else:
            return q0(text[1:])  # Stay in q0 for any other valid symbol ('b')
    else:
        return "rejected"  # Reject if the symbol is not in the alphabet


def q1(text):
    # If the input string is empty, return the current state
    if text == '':
        return 'q1'
    
    symbol = text[0]
    
    # Check if the symbol is 'b'
    if symbol == 'b':
        return q0(text[1:])  # Move back to q0 if 'b' is encountered
    else:
        return q1(text[1:])  # Stay in q1 if the symbol is 'a'


def dfa_ends_with_a(text):
    # Define the final state (we want the string to end in q1, which happens if the last symbol is 'a')
    final_state = 'q1'
    
    # Start the DFA from q0
    state = q0(text)
    
    # Check if the final state is q1 (meaning the string ends with 'a')
    if final_state == state:
        return "Accepted"
    else:
        return "Rejected"


# Test the DFA with a sample input
print(dfa_ends_with_a('abba'))  # Output: Rejected
print(dfa_ends_with_a('a'))     # Output: Accepted
print(dfa_ends_with_a('ab'))    # Output: Rejected
print(dfa_ends_with_a('abaa'))  # Output: Accepted


# change to roman from any base

# Helper function to convert integers to Roman numerals
def to_roman(n):
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    roman = ''
    for value, numeral in roman_numerals:
        while n >= value:
            roman += numeral
            n -= value
    return roman

# Function to check if a character is valid for the given base
def is_valid_in_base(char, base):
    if char.isdigit():  # For '0'-'9'
        return int(char) < base
    elif char.isalpha():  # For 'A'-'Z' (only supports up to base 36)
        return ord(char.upper()) - ord('A') + 10 < base
    return False

# Function to convert a string in a particular base to an integer
def convert_to_integer(input_string, base):
    number = 0
    for char in input_string:
        if not is_valid_in_base(char, base):
            return -1  # Invalid character for the given base
        if char.isdigit():
            digit_value = int(char)
        else:
            digit_value = ord(char.upper()) - ord('A') + 10
        number = number * base + digit_value
    return number

# Function to convert string in a particular base to Roman numeral
def base_to_roman(input_string, base):
    # Step 1: Convert input string from the given base to an integer
    number = convert_to_integer(input_string, base)
    
    # If the number is invalid (negative), return an error
    if number < 0:
        return f"Invalid input '{input_string}' for base {base}"

    # Step 2: Convert the integer to a Roman numeral
    if number <= 0:
        return "Roman numerals can only represent positive integers"
    
    return to_roman(number)

# Example usage:
input_string = "3999"  # Example input in base 16
base = 10           # Base of the input string (hexadecimal)

# Convert the input string "A" in base 16 to a Roman numeral
roman_numeral = base_to_roman(input_string, base)
print(roman_numeral)  

