from main import User, Authentication

#Create a test account and print to attributes
testAccount = User('John', 'Wall1234')
print(testAccount.password)
print(testAccount.username)

#use the change password method and print the result to confirm
testAccount.change_password('Changed1234')
print(testAccount.password)


