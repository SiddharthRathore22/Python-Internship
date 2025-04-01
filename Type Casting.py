#int
print("-----------")
print(3.14)
print(int(3.14))
print(int("10"))
print(int(True))

#Float
print("-----------")
print(float(3))
print(float(True))
print(float('10.5'))



#str
print("-----------")
print(str(123))
print(str(123.23))
print(str(True))


#Bool
print("-----------")
print(bool(1))
print(bool(123233))
print(bool(-12342))
print(bool(0))
print(bool(0.0))
print(bool(4567.32))
print(bool('sid'))
print(bool("S"))
print(bool(''))
print(bool('64363381'))


#Exception

print(int(float('3.14')))
print(float(int(3.14)))
print(type(23))
print(type(23.5))
print(type('str'))
print(type(True))
print('Python is great'.find('is'))




# Implicit typecasting from int to float
integer_number = 5
float_number = 3.14
result = integer_number + float_number
print(result)
# The integer is implicitly converted to a float before the addition.



# Implicit typecasting from int to string
integer_number = 10
string_number = "5"
result = integer_number + string_number
#print(result)  # Output: TypeError (unsupported operand type(s) for +)

