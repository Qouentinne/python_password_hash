import string
from hashlib import sha256
from getpass import getpass
from random import randint, sample
import json

repeat_prompt = True

SALT_SHAKER = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + list(string.punctuation)

def get_pwd():
    clear_pwd = getpass(prompt="Entrez votre mot de passe\n ")
    check_pwd = getpass(prompt="Confirmez votre mot de passe\n ")
    return (clear_pwd, check_pwd)

def check_pwd_creation(passwords):
    if passwords[0] == passwords[1]:
        return False
    else:
        return True

def generate_salt():
    global SALT_SHAKER
    salt_size = randint(15, 25)
    salt = sample(SALT_SHAKER, salt_size)
    return "".join(salt)


while repeat_prompt:
    choice = input("Souhaitez-vous\n 1. Ajouter un utilisateur?\n 2. Vous connecter?\n")
    if choice == '1' or '2':
        repeat_prompt = False

if choice == '1':
    login = input("Définissez votre nom d'utilisateur\n")
    passwords = get_pwd()
    while check_pwd_creation(passwords):
        passwords = get_pwd()

    salt = generate_salt()

    h = sha256()
    h.update((passwords[0] + salt).encode())
    h.hexdigest()

    print(h)