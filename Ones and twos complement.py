def ones_complement(binary):
    result = ""
    
    for bit in binary:
        if bit == '0':
            result += '1'
        elif bit == '1':
            result += '0'
        else:
            return "Invalid binary string"
    
    return result

def twos_complement(binary):
    # Step 1: 1's complement
    ones = ones_complement(binary)

    # Step 2: Add 1
    result = list(ones)
    carry = 1

    for i in range(len(result) - 1, -1, -1):
        if result[i] == '1' and carry == 1:
            result[i] = '0'
        elif result[i] == '0' and carry == 1:
            result[i] = '1'
            carry = 0

    return "".join(result)

binary=input("Enter a Binary Number ")

print("1's complement:", ones_complement(binary))
print("2's complement:", twos_complement(binary))