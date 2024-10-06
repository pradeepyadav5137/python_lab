def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def sin_series(x, n):
  
    if n == 0:
        return 0

    term_index = n - 1
    sign = -1 if term_index % 2 else 1  
    current_term = sign * (x ** (2 * term_index + 1)) / factorial(2 * term_index + 1)
    
  
    return current_term + sin_series(x, n - 1)


x = float(input("Enter the value of x in radians: "))
n = 5  

result = sin_series(x, n)


print(f"The sum of the sine series up to {n} terms for sin({x}) is: {result}")