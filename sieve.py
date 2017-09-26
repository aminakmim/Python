import math
def sieve(a):
    upto_a = [(i+1) for i in range(a)]
    upto_a.remove(1)
    n = int(math.sqrt(a)) + 1
    
    for i in range(2,n):
        print("i :",i)
        if i in upto_a:
            j = 2
            while True:
                m = j*i
                if (m > a):
                    break
                if m in upto_a:
                    upto_a.remove(m)
                j += 1
    return upto_a

print(sieve(100))
