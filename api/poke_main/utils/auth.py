from .db_entry import *
import random
import string


def random_string(string_length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def create_uid(uname, pwd):
    hash_input = "{}{}".format(uname, pwd).encode('utf-8')
    hash_output = hashlib.md5(hash_input).hexdigest()
    return hash_output


def create_random_uid():
    hash_input = random_string().encode('utf-8')
    hash_output = hashlib.md5(hash_input).hexdigest()
    return hash_output


def verify_uid(hash, uname, pwd):
    return hash == hashlib.md5("{}{}".format(uname, pwd).encode('utf-8')).hexdigest()

def login_internal(uname, pwd):
    """
    Returns the user if exists, otherwise None
    :param uname: username of user
    :param pwd: password
    :return: user object of the credentials
    """
    uid = create_uid(uname, pwd)
    user = get_user(uid)
    if user is None:
        print("Username or password is invalid!")
    return user