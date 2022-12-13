# Write a python program which will keep adding a stream of number inputted by the user. The addind stop as soon as user inter "q" for quit.
sum=0
while(True):
    userInput=input("Enter the price: \n")
    if (userInput!='q'):
        sum=sum+int(userInput)
        print(f"Order total so far: {sum}")
    else:
        print(f"Your Bill is {sum}. Thanks for shopping with us")
        break