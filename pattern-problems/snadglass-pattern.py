n = int(input())
k=0
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end="")
    for j in range(1,n-i+2):
        print("*",end=" ")
    print()
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

output:
4

* * * * 
 * * * 
  * * 
   * 
   * 
  * * 
 * * * 
* * * * 
