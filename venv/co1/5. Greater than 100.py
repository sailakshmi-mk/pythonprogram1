list=[]
n=int(input("enter no of items in list"))
for x in range(n):
    x=int(input("enter the items"))
    if x>100:
        list.append("over")
    else:
        list.append(x)
        print(list)