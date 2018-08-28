# intreverse.py

def intreverse(n):
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    
    return(rev)


if __name__ == "__main__":
    print(intreverse(78378))