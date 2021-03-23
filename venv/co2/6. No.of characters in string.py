string=input("string enter")
count=0
for i in range(len(string)):
    if(string[i]!=''):
        count=count+1
print("no of character is:",count)