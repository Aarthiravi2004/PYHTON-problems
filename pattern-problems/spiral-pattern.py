n = int(input())
k=0
for i in range(1,n*2):
    for j in range(1,n*2):
        
        k= (n+1)-(min(min(i , j) ,min((n*2)-i,(n*2)-j)))
        print(k,end=" ")
    print()

output:
n=4
4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 

