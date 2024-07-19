#A string is a chain of character

#Declaring some strings 

str_1  = "Hello World !"

str_2 = "My names is "

str_3 = "Wedson"

#Display the output 

print(str_1)

print(str_2)

print(str_3)

#4 way to display the output or to print the result

print(str_1 + " " + str_2 + " " + str_3 + ".")

print(f"{str_1} {str_2} {str_3}.")

print("%s" %str_1, str_2, str_3,".")

print(str_1,str_2,"",str_3,".")

#Slice in strings 

#Get the first letter in a string 
get_first_l = str_3[0]

print(f"The first letter in {str_3} is : '{get_first_l}'.")
#Get the las letter

get_last_l = str_3[-1]

print(f"The last letter of {str_3} is '{get_last_l}'.")

#Convert to capital(Upper) and lower

name = "james Carry"
#Convert name to capital

cap_name_ = name.upper()

print(f"the capital of name is : {cap_name_}")

#Slice and Capital

cap_name = name[5:].upper()
print("Slice and capital :", cap_name)

#mm = name.join(["a","y"])

#Replace a letter in a string

nom = "Jimmy Paul Peton"

#Replace the letter Jimmy to Tommy

cor_name = nom.replace("Jimmy", "Tommy")

print(cor_name)

#Let's split a text

split_text = name.split("'")

print(f"The split text is {split_text}") 


#Verify if a string startwith a specific letter

start_with_1 = cor_name.startswith("T")

start_with = cor_name.startswith("H")

#Return True if the nme is start with "T" otherwise return false

print(start_with_1)

print(start_with)


#There are a lot of thing that we can do with a string. type help(str) to see or dir(str)

l_d = dir(str)

l_d_1 = help(str)


