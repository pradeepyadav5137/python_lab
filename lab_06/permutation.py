def permute(s, answer):
    if len(s) == 0:
        print(answer)
        return

    for i in range(len(s)):
        char = s[i]
        left_substr = s[0:i]
        right_substr = s[i+1:]
        rest = left_substr + right_substr
        permute(rest, answer + char)

# Example usage
string =input("enter string")
permute(string, "")
