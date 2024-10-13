def get_first_n_chars(s, n, index= 0):
    # Base case: if index reaches n, return an empty string
    if index == n:
        return ""
    
    # Recursive case: return current character + recursive call for the next character
    return s[index] + get_first_n_chars(s, n, index + 1)

def get_last_n_chars(s, n, index=None):
    # Initialize index to the length of the string - n if it's the first call
    if index is None:
        index = len(s) - n
    
    # Base case: if n is 0, return an empty string
    if n == 0:
        return ""
    
    # Recursive case: return current character + recursive call for the next character
    return s[index] + get_last_n_chars(s, n - 1, index + 1)

# Test the functions
s = "WARPFRAME"
n = 3
first_n_chars = get_first_n_chars(s, n)
last_n_chars = get_last_n_chars(s, n)
print("First", n, "characters:", first_n_chars)
print("Last", n, "characters:", last_n_chars)
