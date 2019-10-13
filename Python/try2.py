def add_to_list(list2,n):
    L=len(list2)
    x=0
    while(x<L):
        list2[x]+=2
        x=x+1

    return list2



list1 = [10, 5, 2, 6, 9, 11, 23]

print(add_to_list(list1,2))
