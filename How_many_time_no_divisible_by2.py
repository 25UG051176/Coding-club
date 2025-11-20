l=list(map(int,input("ENTER Numbers").split()))
x=[]
for i in l:
    count=0
    while True:
        if(i%2==0):
            count+=1
            i=i/2
        else :
            break
    x.append(count)
print(max(x))
