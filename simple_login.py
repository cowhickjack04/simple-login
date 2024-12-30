usernames = ["redwards"]
passwords = ["12345"]

while True:
    username = input("Create username: ")
    if username in usernames:
        print("Username already exists, please try again.")
    else:
        print("User created: ", username)
        usernames.append(username)
        break

password = input("Create password: ")
print("Password created: ", password)
passwords.append(password)

print(usernames,",", passwords)

while True:
    login_username = input("Enter username: ")
    if login_username in usernames:
        username_index = usernames.index(login_username)

        login_password = input("Enter password: ")

        if login_password == passwords[username_index]:
            print("Login successful! Welcome, ", login_username, "!")
            break
        else:
            print("Login failed. Please try again.")
    else:
        print("Username not found, please try again.")