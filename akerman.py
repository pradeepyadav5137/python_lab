def akerman(m,n):
     if m == 0:
          return  n+1
     elif m > 0 and n == 0:
          return akerman(m-1, 1)
     elif m>0 and n>0:
          return akerman( m-1 , akerman( m, n-1))

m = int(input(" Enter the value of M :"))
n = int(input(" Enter the value of N :"))

print(f"The value of akermann's function A({m},{n})is {akerman(m,n)} ")



# Enter the value of m: 2
# Enter the value of n: 3
# The value of Ackermann's function A(2, 3) is 9

#  Enter the value of M :3 
#  Enter the value of N :5
# The value of akermann's function A(3,5)is 253   