lst = [[1,2,3],[4,5,6],[7,8,9]]
print(lst)


#Accessing the list

print(lst[0][0])
print(lst[1][1])
print(lst[2][2])
print("-"*20)


#Modify the Values

print(lst)
print(lst[1][1])
lst[1][1] = 9
print(lst[1][1])
lst[1] = ['Siddharth','22']
print(lst)
print("-"*20)

#Appending the Values

print(lst)
lst.append([9,10,11])
print(lst)
print("-"*20)

#Deleting the values

print(lst)
del lst[0]
print(lst)
print("-"*20)


#Deleting the values

lst = [1,2,3,4,5,[1,2,3],6]
print(lst)
print(len(lst))
print("-"*20)

#Reverse the values 
lst = ([1,2,3],[4,5,6],[7,8,9])
print(lst[::-1])


#Find Maximum value i 2d list 
matrix = [
    [3, 5, 9],
    [7, 1, 4],
    [8, 6, 2]
]

max_value =max (max(row) for row in matrix)
print("Maximum value:", max_value)
