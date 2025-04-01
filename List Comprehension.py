lst = [1,2,3,4,5,6]
print(lst)
lst = [i**2 for i in lst]
print(lst)
lst = [i**2 for i in lst]
print(lst)
print('-'*20)


#Finding first 10 even numbers
print([i for i in range(21) if i%2 == 0])
print('-'*20)

#Finding first 10 even numbers and square of it 
print([i**2 for i in range(21) if i%2 == 0])
print("-"*20)


#Multi-Multidimensional List

print([[j for j in range(2)] for i in range(3)])



#Accessing the multi - dimensional list 
lst = [[1,2,3],[4,5,6],[7,8,9]]
print([j for i in lst for j in i])