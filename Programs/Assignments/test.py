lst=[2,3,1,5,6,7,8,3,1,5,3,4]
dup=[]
for i in range(0,len(lst)):
    if lst[i] not in dup:
         dup.append(lst[i])
         
print('Duplicate integers',dup)

print(list([i for i in lst if lst.count(i) >= 2]))
