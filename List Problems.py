# To interchange first and last elements in a 
List = [1,2,3,4,5,6,7,8]
List[0],List[-1]=List[-1],List[0]
print(List)
print('_'*20)

#Swapping of a List 
lst = [1,3,5,7,9]
lst[1],lst[4] = lst[4],lst[1]
print(lst)
print('_'*20)

#Swapping of a list using Temp 
print(lst)
temp = lst[2]
lst[2] = lst[4]
lst[4]= temp
print(lst)
print('_'*20)


#To check if element exists in a list

List = [4,5,6,3,25,6,54,4,3,2]
if 9 in List:
    print(List.index(9))
else:
    print("No")
print('_'*20) 
    
    
#Reversing a List 
List = [10,20,30,40,50]
List.reverse()
print(List)
print('_'*20)

#Reverse Using Slicing
print(List)
print(List[::-1])
print('_'*20)

#Reverese using Reversed
print(List)
Rev = list(reversed(List))
print(Rev)