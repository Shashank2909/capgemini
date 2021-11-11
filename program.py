n=int(input())
list1=list(map(int,input().split()))

for item in list1:
    list2=list(str(item))
    list3=[int(item) for item in list2]
    print(sum(list3),end=" ")
    
