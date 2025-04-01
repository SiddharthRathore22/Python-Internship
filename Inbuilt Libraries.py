import math

x = 10.9
print(math.ceil(x))
print(math.floor(x))
print(math.trunc(x))
print("-"*30)


x = 3
print(math.exp(x))
print(math.log(x))
print("-"*30)


x = 90
print(math.sin(x))
print(math.cos(x))
print(math.tan(x))
print("-"*30)


print(math.pi)
print(math.e)
print(5,math.factorial(5))
print("-"*30)


#Random
import random

print(random.random())
print(random.randint(1,11))
print(random.choice([1,2,3,4,5]))
print(random.sample([1,2,3,4,5],5))
print(random.uniform(1.0,3.0))
print("-"*30)


#Date Time

import datetime
print(datetime.datetime.now())
print(datetime.datetime(2025,2,26,13,5,00))
print(datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))



date_1 = datetime.datetime(2025,3,27,17,17,55)
print(date_1)
date_2 = datetime.datetime.now()
print(date_2)
print(date_1 - date_2)
print("-"*30)


#collections

from collections import Counter, defaultdict, OrderedDict

lst  = [1,2,3,4,5,5,5,6,6,7]
print(Counter(lst))
print("-"*30)


d = defaultdict(int)

d['a'] += 2
print(d)
print("-"*30)


d = OrderedDict()

d['one'] = 1
d['two'] = 2
print(d)


#strings
import string

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print("-"*30)

print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print("-"*30) 


print(string.punctuation)
