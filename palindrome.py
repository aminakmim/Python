def is_palindrome(a):
    b = a[::-1]
    return (b==a)

q = None

while(q!= "q"):
    x = str(input("\nEnter the string :"))
    p = is_palindrome(x)
    s = "is palindrome." if p else "is not palindrome."
    print(x,s)
    q = input("Press q to exit , any other key to continue :")
