#Declare an integer and float

int_1 = 2

int_2 = 4

int_3 = 7

#Operation between integer

somme = int_1 + int_2

mult = int_3 * int_2

div = mult / somme 

print(int_1, int_2, int_1+int_3)

print(f"The result of the division is : {div}")

print(f"The result of the addition is : {somme}")

print(f"The result of the multiplication is : {mult}")

print("")


#Declaring float

fl_1 = 12.5

fl_2 = 23.4

fl_3 = 19.5

#Operarion between float

som = fl_1 + fl_2

mul = fl_2 * fl_2

print("The result of two float is :",som)
print("The result is %s"%mul)

#Convert integer to float or float to integer

conv1 = float(int_2)

print(conv1)

conv2 = int(fl_3)

print(conv2)

#Double check the two result conv1 and conv2

print("Conv1 is a float = ",conv1, "and Conv2 is an integer = ",conv2)

#Note conv2 was an float 19.5, we convert it to an integer, 19

n = 5
n.pow(2)
