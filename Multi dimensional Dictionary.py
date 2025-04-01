dict = {1: {'Name' : 'Sid','Roll.No': 12345},
        2: {'Name': 'Ankur','Roll.No':23344},
        3: {'Name': 'Ashish','Roll.No':34452}
}
print(dict)
print('-'*50)

#Accessing the Elements
print(dict[1],'\n',dict[2])
print(dict[1]['Roll.No'])
print('-'*50)

#Adding the values
print(dict)
dict[4] = {'Name': 'Prakash','Roll.No':2567544 }
print(dict)
print('-'*50)



# updating the values
print(dict)
dict[3]['Name'] = 'Avneet'
print(dict)
print('-'*50)

#deleting the values

print(dict)
del dict[4]
print(dict)
print('-'*50)


#Going through the data
print(dict)
for i in dict.keys():
    print(i,dict[i]['Name'],dict[i]['Roll.No'])
print('-'*50)


#Goin to deeper with marks

Data = dict = {1: {'Name' : 'Sid',      'Roll.No': 12345,    'Marks':{'Hin': 45,'Eng':62,'Maths':78}},
               2: {'Name': 'Ankur',     'Roll.No':23344,     'Marks':{'Hin': 67,'Eng':57,'Maths':88}},
               3: {'Name': 'Ashish',    'Roll.No':34452,     'Marks':{'Hin': 35,'Eng':72,'Maths':98}},
}

print(Data)

for i in Data.keys():
    print(i,Data[i]['Name'], Data[i]['Marks']['Hin'])
for j in Data.keys():
    print(j,Data[j]['Roll.No'],Data[j]['Marks']['Maths'])
    
for k in Data.keys():
    print(k,Data[j]['Marks'])