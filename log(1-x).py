def logn_series( x, n):
        if n == 0:
                return 0
        term_index = n-1
        current_term = (x ** ( term_index +1) )/ (term_index +1)

        return current_term + logn_series(x , n-1)

                                        
x = float(input("Enter the value of x so that -1<= x <1 : "))
if  x< -1 or x>= 1:
        print("Invalid value of x")
else:
        n = int(input("Enter the value of number of terms :"))

result = -1 * logn_series(x , n)

print(f"The sum of the log(1-x) series till {n} terms when x is log(1-{x}) : {result} ")



# Enter the value of x so that -1 <= x < 1: 0.5
# Enter the number of terms: 5
# The sum of the log(1-x) series up to 5 terms for log(1-0.5) is: -0.8958333333333333
