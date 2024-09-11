# 1 -> 100
# for i in range(100):
#     print(i)

# n = int(input("No. = "))
# for i in range(10):
#     print(i,"*",n,"=", n*i )


# for e in range(100 , 0 , -1):
#     print(e)
# 1.	Write a program to repeatedly check for the largest number until the user enters “done”. 

num = []
while True:
    i = int(input("Enter no. = "))
    a = int(input("Enter 0 if done or continue enter 1 = "))
    num.append(i)
    if(a == 0):
        break

num.sort()
a = len(num)
print(num[a-1])