#While loop

# n = 30
# i = 1
# s = 1

# while(n>s):
#     print(s) # 1 , 3 , 6 , 10
#     i= i+1 #  2 , 3 , 4 , 5
#     s = s + i  # 3, 6, 10, 15 , 
    
#Nested While loop
# outer_counter = 1
# while outer_counter <= 3:
#     inner_counter = 1
#     while inner_counter <= 2:
#         print(f"({outer_counter}, {inner_counter})", end=' ')
#         inner_counter += 1
#     outer_counter += 1
    
# outer_counter = 1
# while outer_counter <=3:
#     inner_counter = 1
#     while inner_counter <= 2:
#         print(f"({outer_counter},{inner_counter})", end=' ') # (1,1),(1,2),
#         inner_counter += 1   #(2), (3), 
#     outer_counter += 1 
    
    
    
numbers = []

while True:
    user_input = input("Enter a positive number (enter a non-positive number to stop): ")

    # Check if the input can be converted to a float and is non-negative
    if user_input.replace('.', '', 1).isdigit() and float(user_input) > 0:
        numbers.append(float(user_input))
    elif user_input.replace('-', '', 1).isdigit() and float(user_input) <= 0:
        break  # Exit the loop if a non-positive number is entered
    else:
        print("Invalid input. Please enter a valid positive number.")

# Data handling after the loop
if numbers:
    print(f"You entered the following positive numbers: {numbers}")
else:
    print("No positive numbers were entered.")