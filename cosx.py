def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def cos_series(x, n):
  
    if n == 1:
        return 1

    term_index = n - 1
    sign = -1 if term_index % 2 else 1  
    current_term = sign * (x ** (2 * term_index)) / factorial(2 * term_index)
    
  
    return current_term + cos_series(x, n - 1)


x = float(input("Enter the value of x in radians: "))
n = int(input("Enter the number of terms of the series :")) 

result = cos_series(x, n)


print(f"The sum of the cosine series up to {n} terms for cos({x}) is: {result}")




# Enter the value of x in radians: 1.57
# Enter the number of terms of the series: 5
# The sum of the cosine series up to 5 terms for cos(1.57) is: 0.0007963150837744046