# write a program to print the following number type using loop
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1
# 1
n=int(input())
for i in range(0,n+1):
    for j in range(n-i,0,-1):
        print(j,end=" ")
    print()




