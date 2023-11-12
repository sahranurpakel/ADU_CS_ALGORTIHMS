# https://leetcode.com/problems/fibonacci-number/
def fibonacci(n):
    if n == 1 or n == 0 :
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
