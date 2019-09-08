import bcrypt


def hash_password(password):
    password = password.encode()
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password.decode()


def is_match(password, hash):
    password = password.encode()
    hash = hash.encode()
    return bcrypt.hashpw(password, hash) == hash
