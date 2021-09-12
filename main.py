import bcrypt

original_password = input("Enter your Original Password: ")
password = bytes(original_password,encoding='utf-8')
hashed = bcrypt.hashpw(password,bcrypt.gensalt())
print("Password saved Successfully!")
print(hashed)

def save():
    data = hashed