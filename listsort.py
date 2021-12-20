def Binarysearch(list1,key):
    found=False
    low=0
    high=len(list1)-1
    while low<=high and not found:
        mid=(low+high)/2
        if key == list1[mid]:
            found = True

        elif key>list1[mid]:
            low=mid+1
        else:
            high =mid-1
    
    if found ==True:
        print("Key  is found")
    else:
        print("Key not found")



list1= [25,5,3,9,31,7,1]
list1.sort()
print(list1)
key=int(input("Enter the key number"))
Binarysearch(list1,key)