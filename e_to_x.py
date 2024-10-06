def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def exponent_series(x, n):
  
    if n == 1:
        return 1
    
    term_index = n - 1
   
    current_term =(x ** (term_index)) / factorial(term_index)
    
  
    return current_term + exponent_series(x, n - 1)



x = int(input("Enter the value of x :"))
n = int(input("Enter then number of the terms : ")) 

result = exponent_series(x, n)


print(f"The sum of the exponent series up to {n} terms for exp({x}) is: {result}")




# Enter the value of x: 2
# Enter the number of terms: 5
# The sum of the exponent series up to 5 terms for exp(2) is: 7.0



# Enter the value of x: 1
# Enter the number of terms: 5
# The sum of the exponent series up to 5 terms for exp(1) is: 2.708333333333333