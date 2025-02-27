# while loop is used to execute a block of staements repeatedly until a given condition is satisfied

count = 0

while count <9:
    print(count)
    count +=1 

# using user imput.

password = "1234"

user_input = ""
while user_input != password:
    user_input = input("Enter the password again: ")

print("Access granted")
