# enter a name
# -> Welcome to comprog + name 

user_input = input("Enter name: ")
letter = 0 

for j in user_input:
    letter += 1

print(f'{user_input}')
print(f'{letter}')