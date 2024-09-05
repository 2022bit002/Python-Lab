def binary_subtraction(bin1, bin2):
    # Ensure both binary strings are of the same length by padding with zeros
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)

    result = ''
    borrow = 0

    # Traverse the binary strings from right (least significant bit) to left (most significant bit)
    for i in range(max_len - 1, -1, -1):
        b1 = int(bin1[i])
        b2 = int(bin2[i])

        # Adjust for any borrowed value
        b1 -= borrow

        if b1 < b2:
            # Borrow from the next higher bit
            b1 += 2
            borrow = 1
        else:
            borrow = 0

        # Perform the subtraction and append the result
        result = str(b1 - b2) + result

    # Remove leading zeros from the result
    result = result.lstrip('0')

    # If result is empty, it means the result is 0
    return result if result != '' else '0'

# Example usage:
bin1 = "1010"  # 10 in decimal
bin2 = "110"   # 6 in decimal

result = binary_subtraction(bin1, bin2)
print(f"{bin1} - {bin2} = {result}")  # Output: "100" (which is 4 in decimal)


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

    # Traverse the numbers from right to left (least significant digit to most significant)
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
print(f"{num1} - {num2} = {result}")  # Output: "3643"

