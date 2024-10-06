def logp_series(x, n):
  
    if n == 0:
        return 0
    
    term_index = n - 1
    sign = -1 if term_index % 2 else 1  
    current_term = sign * (x ** (term_index+1)) / (term_index+1)
    
  
    return current_term + logp_series(x, n - 1)



x = float(input("Enter the value of x (-1 < x <= 1): "))
if x <= -1 or x > 1:
    print("The series does not converge for given value of x x ")
else:
    n = int(input("Enter the number of terms: "))


result = logp_series(x, n)


print(f"The sum of the log(x+1) series up to {n} terms for log(1+{x}) is: {result}")


# Enter the value of x (-1 < x <= 1): 0.5
# Enter the number of terms: 5
# The sum of the log(1+x) series up to 5 terms for log(1+0.5) is: 0.4054651081644433