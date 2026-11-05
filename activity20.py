from getpass import getpass

user1 = "bensaw"
password = "pogimeses"

isLogin = False

while isLogin == False:

  username = input("Please input your username ---> ")
  passsword = input("Please input your password --->")

  if username == user1 and password == password:
    print("LOGIN SUCCESFULLY")
    isLogin = True
  else:
    print("LOGIN DENIED")
    isLogin = False

