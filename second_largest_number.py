list = [0,20,19,45,20]
smax=max = 0
for i in list:
    if(max<i):
        max=i
    elif(i<max):
        smax=i
print("largest Number",max)
print('second largest Number',smax)