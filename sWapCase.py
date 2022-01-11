def swapcase(s):
    x=""
    for c in s:
        if c.isupper():
            c=c.lower()
        else:
            c=c.upper()
        x+="".join(c)
    return x    
    
if __name__ == '__main__':

        
    s=input("Enter the string")
    result=swapcase(s)
    print(result)