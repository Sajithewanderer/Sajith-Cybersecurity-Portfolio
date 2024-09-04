
# open, read and split a text file
with open("login_attempts.txt", "r") as file:
    file_text = file.read()
usernames = file_text.split()
print(usernames)


# Create a function that counts a user's failed login attempts
def login_check(login_list, current_user):
    counter = 0
    for i in login_list:
        if i == current_user:
            counter = counter + 1
    if counter >= 3:
        return print("You have tried to login three or more times. Your account has been locked.")
    else:
        return print("You can login in!")


login_check(usernames, "Basha")
