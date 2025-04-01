#Exception handling

try:
    x = 10
    print(1)
    print(x/0)
    print(2)
except:
    print("Error occured")
print("-"*50)
    
    
    
#Exceptions with specific errors

try:
    num = 0
    # print(num/0) #output - Zero is in the divisor
    # print(num*0) #output - 0
    print(int('e23')) # output - Unknown error
except ZeroDivisionError:
    print('Zero is in the divisor')


except:
    print('Unknown Error')
    
    
    
#Final Exception Handling


try:
    num1, num2 = 10,0
    print(num1/num2)
    
except ValueError as zde:
    print(zde)
    
except Exception as e:
    print(e)
    
else:
    print('Everything is fine!')
    
    
finally:
    print("program End!")
    
print("-"*50)
    


# Raising Exceptions

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print(f"Your age is {age}")

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except ValueError as ve:
    print(ve)