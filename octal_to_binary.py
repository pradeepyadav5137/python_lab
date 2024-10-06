
def octal_to_binary(octal_num):
    if octal_num == 0:
        return ""
    

    binary_values = ["000", "001", "010", "011", "100", "101", "110", "111"]
    last_digit = octal_num % 10
    
 
    return octal_to_binary(octal_num // 10) + binary_values[last_digit]


octal_num = int(input("Enter an octal number: "))


if octal_num == 0:
    print("Binary equivalent of octal 0 is: 0")
else:
    
    binary_result = octal_to_binary(octal_num)


    print(f"Binary equivalent of octal {octal_num} is: {binary_result}")
