# You want to be safe online and use different passwords for different websites. 
# However, you are forgetful at times and want to make a program 
# that can match which password belongs to which website without storing the actual password!

# This can be done via something called hashing. Hashing is when we take something and 
# convert it into a different, unique identifier. This is done using a hash function. 
# Luckily, there are several resources that can help us with this.

# For example, using a hash function called SHA256(...) something as simple as

# hello

# can be hashed into a much more complex

# 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

# Fill out the login(...) function for a website that hashes their passwords. 
# Login should return True if an email's stored password hash in stored_logins is the same as '
# 'the hash of password_to_check.

# (Hint. You will need to use the provided hash_password(...) function. 
#  You don't necessarily need to know how it works, just know that hash_password(...) '
#  'returns the hash for the password!)


import hashlib

def hash_password(pwd):
    """Hashes a password using SHA256."""
    return hashlib.sha256(pwd.encode()).hexdigest()

def login(user_email, password_to_check, login_data):
    """
    Checks if the hashed password matches the stored hash.
    
    :param user_email: The user's email (key in stored_logins)
    :param password_to_check: The password entered by the user
    :param stored_logins: Dictionary with emails as keys and hashed passwords as values
    :return: True if the password matches, False otherwise
    """
    if user_email in login_data:
        return login_data[user_email] == hash_password(password_to_check)
    return False

# Example usage
stored_logins = {
    "user@example.com": hash_password("securepassword123"),
    "admin@example.com": hash_password("adminpass456")
}

email = input("Enter your email: ")
password = input("Enter your password: ")

if login(email, password, stored_logins):
    print("Login successful!")
else:
    print("Invalid email or password.")
# This code defines a simple login system that hashes passwords for security.
# It uses the SHA256 hashing algorithm to compare hashed passwords without storing them in plain text.