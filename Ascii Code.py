print('A')
print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(ord('0'))
print(ord(' '))
print(ord('!'))
print(ord('#'))
print(ord('`'))
print(ord('~'))
print("-"*50)


#chr
print(chr(65))
print(chr(45))
print(chr(48))
print(chr(97))
print("-"*50)

# write a code to print all the ascii code


for i in range(33,127):
    print(i,chr(i))
print("-"*50)

    
#write a code to   
student_name = 'Ashish'
for i in student_name:
    print(ord(i) + 1)
print("-"*50)


text = 'Python'
ascii_val = [ord(i) for i in text]
print(ascii_val)

text = 'A'
print(chr(ord(text)+ 3))