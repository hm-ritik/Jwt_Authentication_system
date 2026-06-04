from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"] , deprecated="auto")


def hash_password(password:int):
    password_hashed=pwd_context.hash(password)
    return password_hashed

def verify_password(password:int):
    verified_password=pwd_context.verify(password)
    return verified_password