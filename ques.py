# take a input from the user and print it's table
num=int(input("enter the number"))
for i in range(1,11):
    # print(str(num)+"x"+str(i)+"="+str(i*num)) #both are same
    print(f"{num}x{i}={num*i}")                 #both are same
