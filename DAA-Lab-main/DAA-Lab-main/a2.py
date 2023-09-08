import math

def gcd(a, b):
    return math.gcd(a, b)

num1 = int(input("Enter first num: "))
num2 = int(input("Enter secoond num: "))
result = gcd(num1, num2)
print("GCD of", num1, "and", num2, "is", result)
