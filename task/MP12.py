abc = "Sangmyung University"

d={}
num=0

for i in range(len(abc)):
    ans=abc[num]
    num+=1
    if d.get(ans) == None:
        d[ans]=1
    else:
        d[ans] += 1

print(d)
        
    
    
