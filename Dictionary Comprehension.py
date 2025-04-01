# Dictionary Comprehension


dict = {i:i**3 for i in range(1,6)}
print(dict)
print('-'*30)

#dictionaries with the conditions 

dict_1 = {i:i**2 for i in range(1,11) if i%2==0}
print(dict_1)
print('-'*30)


#Dictionaries from List

Lst = ['Apple','Banana','Grapes']
dict_2 = { item : len(item) for item in Lst} 
print(Lst)
print(dict_2)
dict_2 = {len(item):item for item in Lst} 
print(dict_2)
print('-'*30)

#Special keys with strings
dct = {'num_' + str(i) :i for i in range(1,11)}
print(dct)
print('-'*30)

#Shortlisting Based on values

dct = {'num_' + str(i) :i for i in range(1,11)}
dct = {k:v for k,v in dct.items() if v%3==0}
print(dct)
print('-'*30)


matrix = [[1,2,3],[4,5,6],[7,8,9]]
dct_3 = {(i,j): matrix[i][j] for i in range(3) for j in range(3)}
print(dct_3)

dct_3 = { matrix[i][j]:(i,j) for i in range(3) for j in range(3)}
print(dct_3)
