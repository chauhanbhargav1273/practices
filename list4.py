l=[1,2,4,3,6,8,4,2,8]
l1=[]

for i in l:
    if i not in l1 and l.count(i)>1:
        l1.append(i)
print(l)
print(l1)
