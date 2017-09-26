def factors(a):
    p = [i for i in range(1,a)]
    f = lambda x:a%x==0
    fac_list = list(filter(f,p))
    return fac_list
    

q = None

while(q!= "q"):
    x = int(input("Enter the number :"))
    z = factors(x)
    print(z)
    q = input("Press q to exit , any other key to continue :")
