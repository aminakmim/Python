import math

def is_prime(a):
    n = abs(a)
    if (n<2):
        return False
    elif (n%2==0):
        return False
    n1 = int(math.sqrt(n))+ 1
    return all(n%i for i in range(3,n1,2))
    
q = None

while(q!= "q"):
    x = int(input("Enter the number :"))
    p = is_prime(x)
    s = "is prime." if p else "is not prime."
    print(x,s)
    q = input("Press q to exit , any other key to continue :")
