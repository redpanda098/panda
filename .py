str = "Hello"
#   0 1 2 3 4  index
# { H, e, l, l, o } value

# fetching individual character from string
# print(name_of_string[index_number])
print(str[0])  

#slicing
#print(name_of_string[starting_point : ending_point])
print(str[0:4])

#looping of the string
for i in str:
    print(i , end= "")

print("\nusing upper and lower method")

#using upper method
print(str.upper())

#using lower method
print(str.lower())

# numeric types
num1 = 10   #int
num2 = 20.5  #float

#sequence types
text = "Hello World"  #string
fruits = ["apple", "banana", "cherry"]  #list/array

#mapping types JSON :- #dict /obj
student = {
    "name": "student" ,
    "age": 20,
    "skills" : "html"
}

#boolean type
a = True
print("converting the boolen into number:" , int(a))  # using typecasting inorder to change boolean dt in interger

#testing operators
x = 10
y = 20

if x != y:
    print("true")
else:
    print("false")

#integer to  float
num = 10
num_float = float(num)
print("integer to float:", num_float) # output: 10.0

#float to integer
num2 = 20.5
num_int = int(num2)
print("float to integer:", num_int) # output: 20

#string to integer(if string contains numeric )
str_num = "30"
str_to_int = int(str_num)
print("string to integer:", str_to_int) # output: 30

#integer to string
num3 = 40
int_to_str = str(num3)
print("integer to string:", int_to_str) # output: "40"

#arithmetic operators
a = 15
b = 4
print("Addition:", a + b)          # Addition
print("Subtraction:", a - b)       # Subtraction
print("Multiplication:", a * b)    # Multiplication
print("Division:", a / b)          # Division
print("modulus:", a % b)           # Modulus

#comparison operators
print("is a equal to b:", a == b)       # Equal to
print("is a not equal to b:", a != b)   # Not equal to
print("is a greater than b:", a > b)     # Greater than
print("is a less than b:", a < b)        # Less than
