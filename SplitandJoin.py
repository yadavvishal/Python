def split_and_join(s):
    x=s.split()
    print(x)
    y="-".join(x)
    return y
if __name__ == '__main__':
    s = input("Enter the strings:")
    result = split_and_join(s)
    print(result)
