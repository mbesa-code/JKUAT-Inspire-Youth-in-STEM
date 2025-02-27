import hashlib
import os

#file to store the passwords and site names
FILENAME = "passwords txt"

# function to hash the password
def hash_password(password):
    """Hash password for storing."""
    return(hashlib.sha256(password.encode()).hexdigest())

# function save the password
def save_password(site, password):
    """save the site name and the password"""
    hashed_password = hash_password(password)
    with open(FILENAME, 'a') as file:
        file.write(f"{site} {hashed_password}\n")
    print(f"Password for the site {site} saved successfully")

# function to get the password
def get_password(site):
    """Retrieve the password for the site"""
    if not os.path.exists(FILENAME):
        print("No passwords saved yet")
        return
    with open(FILENAME, "r") as f:
        for line in f:
            stored_site, stored_password = line.strip().split(" ")
            if stored_site == site:
                return stored_password
    print(f"No password saved for the site {site}")
    return name

def main():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w" ) as f:
            pass # create the file if it does not exist

    action = input("Enter 'save' to save a password 'get' to retrieve a password: ")

    if action == "save":
        site = input("Enter the site name: ")
        import string
        import random
        # generate a random password
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join (random.choices(characters, k=10))
        print(f"generated password: (password)")
        save_password(site, password)
    elif action == "get":
        site = input("Enter te site name to retrieve password: ")
        password = get_password(site)
        if password:
            print(f"password for the site {site} is {password}")
    else:
        print("invalid action")

if __name__ == "__main__":
    main()