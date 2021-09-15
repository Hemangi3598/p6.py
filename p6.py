# wapp to read three integers and
# print the sum and avg

n1= int(input("enter first num "))
n2= int(input("enter second num "))
n3= int(input("enter third num "))
sum= n1+n2+n3
avg= n1+n2+n3 / 3

print("sum = ", sum)
print("avg = ", avg)
print("avg = ", round(avg,2))
print("avg = ", round(avg,3))
print("avg = ", round(avg,4))
print("avg = ", round(avg,5))
print("avg = ", round(avg,1))

# round() function is to used to round off digits after decimal place
# for eg if o/p is 3.445677776 then after using round() function for 2 we will get o/p as
# 3.4456777776 ---> 3.44
