import time
from timeit import default_timer as timer

def GCD(x, y):
 
    if x > y:
        min = y
    else:
        min = x
    for i in range(1, min + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
             
    return gcd

def euclid_gcd(a, b):
    if(b == 0):
        return a
    else:
        return euclid_gcd(b, a % b)
 
# a = int(input (" Enter the first number: ") )    
# b = int(input (" Enter the second number: "))  

a = 60
b= 48
start = timer()
for i in range(10000):
    res = euclid_gcd(a, b)
end = timer()
print(end - start)

start2 = timer()
for i in range(10000):
    ress = GCD(a,b)
end2 = timer()
print(end2-start2)