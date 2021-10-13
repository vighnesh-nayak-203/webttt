n=int(input("Enter a number less than 1000:"))
d=int(input("Enter number of decimals requaired:"))
def dec_inc(n,d):
    step=1
    guess=0
    k=0
    for i in range(d+1):
        for j in range(1,10):
            k+=1
            if (guess+j*step)**3>n:
                guess+=(j-1)*step
                break
            if j==9:
                guess+=(j)*step
                break
        step=1/10**(i+1)
    print("Cube root of",n,"is",guess,k)
def binary_search(n,d):
    s=0
    e=n
    m=0
    k=0
    while s<=e and abs(m**3-n)>1/10**d:
        m=(s+e)/2
        if m**3>n:
            e=m
        if m**3<n:
            s=m
        k+=1
    print("Cube root of",n,"is",m,k)
def guess_ur_no(n):
    print("Please think of a number between 0 and 100!")
    s=0
    e=100
    g=(s+e)/2
    while s<=e:
        print(f"Is your secret number {g}?")
        a=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        while a!="h" and a!="l" and a!="c":
            print("Sorry, I did not understand your input.")
            print(f"Is your secret number {g}?")
            a=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        if a=="h":
            e=g
        elif a=="l":
            s=g
        else:
            print(f"Game over. Your secret number was: {g}")
            break
        g=int((s+e)/2)
guess_ur_no(41)














