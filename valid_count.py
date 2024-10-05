def decimal_subtraction(num1, num2):
    # Convert inputs to strings to process each digit
    num1 = str(num1)
    num2 = str(num2)

    # Ensure num1 is the larger number or pad the smaller number with leading zeros
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    num2 = num2.zfill(len(num1))  # Pad num2 with leading zeros

    result = ''
    borrow = 0

    # Traverse the numbers from right to left 
    for i in range(len(num1) - 1, -1, -1):
        digit1 = int(num1[i])
        digit2 = int(num2[i])

        # Subtract the borrowed value if any
        digit1 -= borrow

        if digit1 < digit2:
            # Borrow from the next higher digit
            digit1 += 10
            borrow = 1
        else:
            borrow = 0

        # Perform the subtraction and append the result
        result = str(digit1 - digit2) + result

    # Remove leading zeros from the result
    result = result.lstrip('0')

    # If result is empty, return '0' as the final answer
    return result if result != '' else '0'

# Example usage:
num1 = 543
num2 = 1789

result = decimal_subtraction(num1, num2)
#print(f"{num1} - {num2} = {result}")  # Output: "3643"

