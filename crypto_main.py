from cryptography.fernet import Fernet

def NEW_KEY_YNS():
    key = Fernet.generate_key()
    return key

def NEW_KEY_YS():
    key = Fernet.generate_key()
    with open('privateKEY.txt', 'wb') as f:
        f.write(key)
    return 'Файл "privateKEY.txt" с ключом успешно создан'


def encryptedtext(INPUT_CHOICE_key, byte_encrypt_text):
    cipher = Fernet(INPUT_CHOICE_key)
    data = byte_encrypt_text.encode()
    encrypt = cipher.encrypt(data)
    return encrypt


def decryptedtext(INPUT_CHOICE_key, byte_decrypt_text):
    cipher = Fernet(INPUT_CHOICE_key)
    decrypt = cipher.decrypt(byte_decrypt_text.encode())
    c = decrypt.decode()
    return c

#Зашифровано\расшифрован файл
def encryptedfile(INPUT_CHOICE_key, filename):
    cipher = Fernet(INPUT_CHOICE_key)
    with open(filename, "rb") as f:
        data = f.read()
    encrypt = cipher.encrypt(data)
    with open("crypttext.txt.enc", "wb") as fs:
        fs.write(encrypt)
    return 'создан файл "crypttext.txt.enc"'
    
def decryptedfile(input_choice_key, filename):
    cipher = Fernet(input_choice_key.encode())
    with open(filename, "rb") as f:
        data = f.read()
    decrypt = cipher.decrypt(data)
    with open("decrypted.txt", "wb") as f:
        f.write(decrypt)
    return 'создан файл "decrypted.txt"'

