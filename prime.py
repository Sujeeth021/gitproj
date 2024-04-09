n=91
k=0
for i in range(n/2):
    if(n%2==0):
        print("Not a prime")
        k=1
        break
if(k==0):
    print("Prime")