list = [1,2,3,4,5,6,7]
for i in range(0,len(list)-1):
    for j in range(len(list)-1,0,-1):
        if(i<j):
            list[i],list[j]=list[j],list[i]
print(list)
