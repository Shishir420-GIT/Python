import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(5000)

def factorial(num):
    #if num==1:
    #    return 1
    return num*factorial(num-1)

print(factorial(5))