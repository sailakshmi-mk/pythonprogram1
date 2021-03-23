def Merge(dic1,dic2):
    return(dic1.update(dic2))
dic1={'a':10,'b':8}
dic2={'c':6,'d':4}
print(Merge(dic1,dic2))
print(dic1)