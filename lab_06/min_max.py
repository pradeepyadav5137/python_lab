def find_min_char(s, index=0, min_char=None, min_index=None):
    # Base case: if we have reached the end of the string, return min_char and min_index
    if index == len(s):
        return min_char, min_index
    
    # Initialize min_char and min_index if they are None
    if min_char is None or s[index] < min_char:
        min_char = s[index]
        min_index = index
    
    # Recursive call for the next character
    return find_min_char(s, index + 1, min_char, min_index)

def find_max_char(s, index=0, max_char=None, max_index=None):
    # Base case: if we have reached the end of the string, return max_char and max_index
    if index == len(s):
        return max_char, max_index
    
    # Initialize max_char and max_index if they are None
    if max_char is None or s[index] > max_char:
        max_char = s[index]
        max_index = index
    
    # Recursive call for the next character
    return find_max_char(s, index + 1, max_char, max_index)

# Test the functions
s = "pradeep"
min_char, min_index = find_min_char(s)
max_char, max_index = find_max_char(s)

print("Minimum character:", min_char, "at index", min_index)
print("Maximum character:", max_char, "at index", max_index)
