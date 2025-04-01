lst = ['Ashish', 'Ankur', 'Riya','Adarsh','Parag','Awneet']
print(lst)
print(lst[0])
print(lst[4])
print(lst[-1])
print('-'*20)

#convert Negative indexing to positive

print(lst)
print(lst[-4])
print(lst[len(lst)-4])

# Modify Values
print(lst)
lst[2]  = 'sakshi'
print(lst)

#Slicing

print(lst[1:4])
print('-'*20)


#Reverse list
print(lst)
print(lst[::-1])
print('-'*20)

#Reverse list
print(lst)
print(lst[::-2])
print('-'*20)

#Appeding

print(lst)
lst.append("Ankit")
print(lst)
print('-'*20)

#removing
print(lst)
lst.remove("Ankit")
print(lst)
print('-'*20)

#Length
print(lst)
print(len(lst))
print('-'*20)



#sorting
lst = [3,5,6,5,4,3,56,8,1]
print(lst)
print(sorted(lst))
print(lst[::-1])
print('-'*20)


#finding element

lst = ['Ashish', 'Ankur', 'Riya','Adarsh','Parag','Awneet']
print(lst.index('Adarsh'))
print('-'*20)

#count
lst = ['Ashish', 'Ankur', 'Riya','Adarsh','Parag','Awneet']
print(lst.count('Adarsh'))
print('-'*20)



#Extending

lst.extend(['Arpita','Shambhavi','Kritika'])
print(lst)
print('-'*20)



#Finding Maximum and Minimum in the list
lst  = [3,5,6,5,4,3,56,8,1]
print(lst)
print(min(lst))
print(max(lst))


#Iterating through the elemnts of list
print(lst)

for i in lst:
    print(i)
    
print(lst)
for i in range(len(lst)):
    print(i,lst[i])
print('-'*20)


#Iterating through the elemnts of list in reverse order

print(lst)
for i in range(len(lst)-1,-1,-1):
    print(i,lst[i])
print('-'*20)

# sort():
List = [2.0, 24.1, 3.6, 12.0, 4.5]
print(len(List))
List.sort()
print(List)
List.reverse()
print(List)


#inserting the values 

print(List)
List.insert(1,5)
print(List)


#extend

print(List)
m = [2,3,6]
List.extend(m)
print(List)

#Concatanating two Lists
print(List)
k = List + m
print(List)


matrix = [
    [1, 2, 3],   # Row 0
    [4, 5, 6],   # Row 1
    [7, 8, 9]    # Row 2
]

for row in matrix:  # Outer loop (iterates through rows)
    for item in row:  # Inner loop (iterates through columns)
        print(item, end=" ")
    print()  # Moves to the next line after printing a row
