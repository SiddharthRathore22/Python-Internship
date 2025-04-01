#Dictionary

dict = {'Ashish': 1,2:'Avneet',3:'Riya',4:'Ankur',5:'Sakshi',3:'Ankur','1':'Daniel'}
print(dict)
print('-'*100)

#Accessing the element

dct = {1:'Ashish',2:'Avneet',3:'Riya',4:'Ankur',5:'Sakshi'}
print(dct)
print(dct[1])
print(dct.get(1))
print('-'*100)

#Adding and Updating the key-value pairs

print(dct)
dct[6] = 'Sadaf'
print(dct)
del dct[6]
print(dct)
print('-'*100)


#Cleaning the dictionary

print(dct)
dct.clear()
print(dct)
print('-'*100)


# Iterating through the Dictionary

dct = {1:'Ashish',2:'Avneet',3:'Riya',4:'Ankur',5:'Sakshi'}
print(dct)
print(dct.keys())
print(dct.values())

for k in dct.keys():
    print(k)
print(dct.items())

for i in dct.items():
    print(i)
for k,v in dct.items():
    print(k,v)
print('-'*100)


#check if key is present
print(dct)
print(1 in dct)
print('1' in dct)
print('-'*100)

#Updating the dictionaries

dct_1 = {1:'a',2:'b',3:'c',4:'d',5:'e'}
dct_2 = {1:'A',2:'B',3:'C',4:'D',5:'E'}
dct_1.update(dct_2)
print(dct_1)
print(dct_2)
print("-"*100)

#Copy of dictionary

print(dct)
x = dct.copy()
print(x)
print('-'*100)


#Return the value of a specified key
print(dct)
x = dct.get(4)
print(x)
print('-'*100)


#Pop - remove the element

print(dct)
print(dct.pop(3))
print(dct)
print('-'*100)

#Popitem - removes the last inserted key value

dct = {1:'Ashish',2:'Avneet',3:'Riya',4:'Ankur',5:'Sakshi'}
x = dct.popitem()
print(x)
print(dct)
print('-'*100)

#dict.setdefault(key,default= “None”) - set the key to the default value if the key is not specified in the dictionary

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color","Blue")

print(x)
print(car)
print(type(5 / 2))
print(type(5 // 2))


