# take the angle x and y in degrees. your task is to convert them to radians and compute the following expression print the result up to 2 decimal places at the end.
# sin(x)cos(y)+cos(x)sin(y)

# 30
# 60
# 1.00

# 45
# 15
# 0.087

# 0
# 180
# 0.00
import math
x=int(input())
y=int(input())
p=math.radians(x)
q=math.radians(y)
r=math.sin(p)
s=math.cos(q)
t=math.cos(p)
u=math.sin(q)
a=r*s
b=t*u
m=a+b
print("%.2f"%m)