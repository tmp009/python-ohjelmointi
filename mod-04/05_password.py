MAX_ATTEMPTS = 5
attempt = 0
while True:
  attempt += 1

  username = input("Enter username: ")
  password = input("Enter password: ")

  if username == "python" and password == "rules":
    print("Welcome")
    break
  elif attempt >= MAX_ATTEMPTS:
    print("Access denied")
    break
  else:
    print("Incorrect username or password. Please try again.")
