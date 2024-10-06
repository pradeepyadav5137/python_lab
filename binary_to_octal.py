
# def binary_to_octal(binary_num):
#     if binary_num == 0:
#         return ""
    
  
#     binary_values = {'000' : "0", '001': "1", '010' : "2", '011' :"3", '100' : "4", '101' : "5", '110': "6", '111' :"7"}
#     last_digit = binary_num % 1000

#     while len(str(last_digit)) % 3 != 0:
#         nlast_digit = '0' + str(last_digit)
    

#     return binary_to_octal(binary_num // 1000) + binary_values[int(nlast_digit)]


# binary_num = int(input("Enter an octal number: "))


# if binary_num == 0:
#     print("Binary equivalent of octal 0 is: 0")
# else:
  
#     octal_result = binary_to_octal(binary_num)

   
#     print(f"Binary equivalent of octal {binary_num} is: {octal_result}")


# def binary_to_octal(binary_num):
#     # Base case for recursion
#     if binary_num == 0:
#         return ""
    
#     # Dictionary to map 3 binary digits to an octal digit
#     binary_values = {'000': "0", '001': "1", '010': "2", '011': "3", 
#                      '100': "4", '101': "5", '110': "6", '111': "7"}
    
 
#     binary_str = str(binary_num)
    
 
#     while len(binary_str) % 3 != 0:
#         binary_str = '0' + binary_str
    
    
#     last_three_digits = binary_str[-3:]
    
  
#     octal_digit = binary_values[last_three_digits]
    
  
#     return binary_to_octal(binary_str[:-3]) + octal_digit


# binary_num = input("Enter a binary number: ")


# if binary_num == "0":
#     print("Octal equivalent of binary 0 is: 0")
# else:
   
#     octal_result = binary_to_octal(binary_num)

  
#     print(f"Octal equivalent of binary {binary_num} is: {octal_result.lstrip('0')}")


def binary_to_octal(binary_str):
    # Base case for recursion
    if binary_str == "":
        return ""
    
    # Dictionary to map 3 binary digits to an octal digit
    binary_values = {'000': "0", '001': "1", '010': "2", '011': "3", 
                     '100': "4", '101': "5", '110': "6", '111': "7"}
    
    # Pad the binary string with leading zeros to make its length a multiple of 3
    while len(binary_str) % 3 != 0:
        binary_str = '0' + binary_str
    
    # Take the last three digits
    last_three_digits = binary_str[-3:]
    
    # Convert the last three digits to the corresponding octal digit
    octal_digit = binary_values[last_three_digits]
    
    # Recursively process the remaining part of the binary string
    return binary_to_octal(binary_str[:-3]) + octal_digit


binary_num = input("Enter a binary number: ")

if binary_num == "0":
    print("Octal equivalent of binary 0 is: 0")
else:
    # Convert binary to octal using the recursive function
    octal_result = binary_to_octal(binary_num)

    # Strip leading zeros and print the result
    print(f"Octal equivalent of binary {binary_num} is: {octal_result}")

