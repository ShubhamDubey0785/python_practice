def reverse(n) :
    if len(n)==0:
        return n
    return reverse(n[1:]) + n[0]
num =input()
num_string = str(num)
reversed_num = reverse(num_string)
print(reversed_num)