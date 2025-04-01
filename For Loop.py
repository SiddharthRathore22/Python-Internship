# Print table of any number

print("Enter a number: ")
n = int(input())
for i in range (1,11):
    print(n,'x',i,'=',n*i)


# #short approach
for i in range(n,(n*10)+1,n):
    print(i)


# Nested For loop / rolling two dices

for i in range(1,7):
    for j in range(1,7):
        print(i,j)
    print("----")
print("++++++++++++++")


# #rolling three dices
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
         print(i,j,k)
    print("----")
print("++++++++++++++")

# for n in range(1,13):
#     number = 0
#     for i in range(1,7):
#         for j in range(1,7):
#             if (i + j == n):
#                 number = number + 1
#     print(n,'=',round((number/36)*100,2))
print("++++++++++++++")

for n in range(1,19):
    number = 0
    for i in range(1,7):
        for j in range(1,7):
            for k in range(1,7):
                if (i + j + k == n):
                 number = number + 1
    print(n,'=',round((number/216)*100,2))
print("++++++++++++++")

