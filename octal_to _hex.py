
def hex_to_binary(hex_num):
    if hex_num == "":
        return ""
    

    hex_digit = hex_num[0].upper()
    binary_values = {
        '0': "0000", '1': "0001", '2': "0010", '3': "0011",
        '4': "0100", '5': "0101", '6': "0110", '7': "0111",
        '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
        'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"
    }
    
   
    binary_equivalent = binary_values[hex_digit]
    

    return binary_equivalent + hex_to_binary(hex_num[1:])


hex_num = input("Enter a hexadecimal number: ")


if hex_num == "0":
    print("Binary equivalent of hexadecimal 0 is: 0")
else:
   
    binary_result = hex_to_binary(hex_num)

    
    print(f"Binary equivalent of hexadecimal {hex_num} is: {binary_result}")
