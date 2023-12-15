n = int(input())
start=0
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
        start=j-1
    for k in range(1,i):
        print(start,end=" ")
        start-=1
    print()


OUTPUT:
n=5
        1 
      1 2 1 
    1 2 3 2 1 
  1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 
