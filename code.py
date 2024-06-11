import os
import hashlib

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to create a new user
def create_user(username, password):
    users = {}
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as file:
            users = eval(file.read())

    if username in users:
        print("Username already exists!")
        return

    users[username] = hash_password(password)

    with open("users.txt", "w") as file:
        file.write(str(users))

    os.makedirs(username)

    print("User created successfully!")

# Function to authenticate a user
def authenticate(username, password):
    users = {}
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as file:
            users = eval(file.read())

    if username not in users:
        print("Username not found!")
        return False

    return users[username] == hash_password(password)

# Function to upload a file
def upload_file(username, filename, content):
    if not os.path.exists(username):
        print("User not found!")
        return

    with open(os.path.join(username, filename), "w") as file:
        file.write(content)

    print("File uploaded successfully!")

# Main function
def main():
    while True:
        print("\n1. Create User")
        print("2. Authenticate User")
        print("3. Upload File")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            create_user(username, password)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if authenticate(username, password):
                print("Authentication successful!")
            else:
                print("Authentication failed!")
        elif choice == "3":
            username = input("Enter username: ")
            if not os.path.exists(username):
                print("User not found!")
                continue
            filename = input("Enter filename: ")
            content = input("Enter file content: ")
            upload_file(username, filename, content)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
