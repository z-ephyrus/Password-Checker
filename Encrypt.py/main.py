import bcrypt
import getpass

def pass_hasher(password: str)->bytes:
    password_bytes = password.encode('uts-8')
    hashed = bcrypt.hashpw(password_bytes,bcrypt.gensalt())
    return hashed

def pass_check(password : str, hashed : bytes)->bytes:
    password_bytes = password.encode('uts-8')
    return bcrypt.checkpw(password_bytes,hashed)

if __name__ == "__main__":
    print("Password Hasher :\n")

    original = getpass.getpass("Enter Password...\n")
    stored = pass_hasher(original)

    print("Enter next password for validation : \n")
    ip_password = getpass.getpass("Enter next password :\n")
    if pass_check(ip_password,stored):
        print("Password is matching...")
    else:
        print("Password is not matching...")