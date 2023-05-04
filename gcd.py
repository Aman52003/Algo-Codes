a=int(input("enter no. "))
b=int(input("enter no. "))
def gcd(a, b):

    while b != 0:
        a, b = b, a % b
    return a
result = gcd(a, b)
print(result)  
