def find_min_index_recursive(s, start, min_index):
    # Base case: if we reached the end of the string
    if start == len(s):
        return min_index
    
    # Update min_index if we find a smaller character
    if s[start] < s[min_index]:
        min_index = start
    
    # Recursively call for the next character
    return find_min_index_recursive(s, start + 1, min_index)

def lexicographical_sort(s):
    # Base case: if the string is empty or one character, return it
    if len(s) <= 1:
        return s
    
    # Find the index of the smallest character using recursion
    min_index = find_min_index_recursive(s, 0, 0)
    
    # Place the smallest character at the beginning and recursively sort the rest
    smallest_char = s[min_index]
    remaining_chars = s[:min_index] + s[min_index + 1:]
    
    # Recurse with the remaining characters
    return smallest_char + lexicographical_sort(remaining_chars)

# Test the function
s = input("enter the string : ")
sorted_string = lexicographical_sort(s)
print("Sorted string:", sorted_string)
