def greet():
    print("Hello")
    
for i in range(5):
    greet()
print('-'*20)


# Defining the scope of the variable
g_var = 10
def scope():
    l_var = 5
    print(g_var,l_var)
    
scope()
# print(g_var,l_var)
print('-'*20)


#Passing the parameters
def greet(name):
    print("Hello",name)
    
greet("Ashish")
# name = "Ashish"
greet(name = 'Ashish')


#Passing the parameters with print

def subm(a,b):
    print(a,b,a+b)
    
subm(9,5)
subm(a= 9,b = 5)
subm(5,5)




#Return
def subm(a,b):
    return a+b
    
s = subm(10,5)
print(s)



# Multi Return

def multireturn(a,b):
    return a+b,a-b,a*b

s= multireturn(3,4)
print(s)
print(type(s))



# calling Different functions

lst = [1,2,3,4,5]

def sq(lst):
    return [i**2 for i in lst]
def cu(lst):
    return [i**3 for i in lst]

sq(lst)
cu(lst)
print(sq(lst))
print(cu(lst))


lst_1 = sq(lst)
lst_2 = cu(lst)

def final(lst):
    
    lst_1 = sq(lst)
    lst_2 = cu(lst)

    return [lst_1[i] + lst_2[i] for i in range(len(lst_1))]

print(final(lst))