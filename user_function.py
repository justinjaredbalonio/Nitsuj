def register_user():

 	name1 = input('Enter your first name:')
 	name2 = input('Enter your last name:')
 	email = f'{name1}.{name2}@email.com'
 	full = f'{name1}.{name2}'
 	created_user = ({'user_name': full, 'email' :email })

 	print(f'Welcome {full}! Your email is {email}')

 	return created_user

def edit_user(user):
 	name1 = input('Place your new first name: ')
 	name2 = input('Place your new last name: ')
 	newemail = f'{name1}.{name2}@email.com'
 	newfull = f'{name1}.{name2}'
 	newmail={'user_name': newfull, 'email': newfull}

 	print(f' Your editted account is {newfull}')
 
 	return newmail