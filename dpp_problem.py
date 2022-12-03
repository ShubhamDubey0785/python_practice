a=str(input())
b=int(input())

def place_value(a,b):
    if (b>len(a)):
        print("Index out of range")
    else:
        print(a[b-1])
place_value(a,b)
