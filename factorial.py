def fact(n):
    if (n<2):
        return 1
    return n*fact(n-1)

q = None

while(q!= "q"):
    x = int(input("Enter the number :"))
    p = fact(x)
    print("Factorial of ",x," :",p)
    q = input("Press q to exit , any other key to continue :")
