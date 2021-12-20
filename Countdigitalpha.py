string=input("Enter a string:")
def countLetterandDigit(string):
    lcount = dcount =0
    for c in string:
        if c.isalpha():
            lcount+=1
        elif c.isdigit():
            dcount+=1

    return lcount,dcount

lcount,dcount= countLetterandDigit(string)
print("The alphabets are:",lcount)
print("The Digits are:",dcount)

