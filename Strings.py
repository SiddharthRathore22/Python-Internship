# #Concatenation
# print("Siddharth" + " Rathore")
# print("-"*20)


# #String_Replication
# print("Sid"*3)
# print("-"*20)



# #String_Length
# print('Siddharth Rathore')
# print(len('Siddharth Rathore'))
# print("-"*20)


# #String_Slicing
# print('Siddharth Rathore')
# print('Siddharth Rathore'[0])
# print('Siddharth'[-9])
# print('Siddharth'[0:5])
# print("Siddharth Rathore"[10:17])
# print("Siddharth Rathore"[4:])
# print("Siddharth Rathore"[:7])
# print("Siddharth Rathore"[-9:-1])
# print("-"*20)


# #String Case Conversion
# print("Siddharth Rathore")
# print("Siddharth Rathore".lower())
# print("Siddharth Rathore".upper())
# print("-"*20)


# #String Stripping
# print("Siddharth Rathore")
# print("       Siddharth Rathore     ".strip())
# print("Siddharth        Rathore   ".strip())
# print("-"*20)


# #String Replacing
# print("Siddharth Rathore")
# print("Siddharth Rathore".replace('d','-'))
# print("Siddharth Rathore".replace('Rat','-'))
# print("Siddharth        Rathore   ".replace(' ',''))


# #String Count
# print("SiDdharth Rathore")
# print("SiDdharth Rathore".count('i'))
# print("SiDdharth Rathore".lower().count('d'))


# #String Finding

# print("Siddharth Rathore")
# print("Siddharth Rathore".find('Rat'))


# #String Check

# print('Siddharth')
# print('Siddharth'.isalpha())
# print('123'.isdigit())
# print('siddharth'.islower())
# print('SIDDHARTH'.isupper())



# #String Capitalization

# print('siddharth rathore'.capitalize())
# print('siddharth rathore'.title())


# #Check with tart and end

# print('Siddharth Rathore'.startswith('Sid'))
# print('Siddharth Rathore'.endswith('ore'))


# #

# print('Siddharth Rathore'.center(20,'-'))
# print('Siddharth Rathore'.ljust(20,'-'))
# print('Siddharth Rathore'.rjust(20,'-'))


# string = "python program run on python IDLE, in pythonic way."
# count = string.count("python")
# print(count)


def changeCase(s):
    capitalized = s[0].upper() +s[1:]
    #return capitalized
    print(capitalized)
    
    uppercase = s.upper()
    print(uppercase)
    
# t = int(input())

# for _ in range(t):
s= "hello"
changeCase(s)