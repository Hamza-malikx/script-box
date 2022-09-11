# import base64
# import hashlib
# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes

# _key_ = hashlib.sha256(b'abdullahtayyabha').digest()

# def encrypt(raw):
#     BS = AES.block_size
#     pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

#     raw = base64.b64encode(pad(raw).encode('utf8'))
#     iv = get_random_bytes(AES.block_size)
#     cipher = AES.new(key= _key_, mode= AES.MODE_CFB,iv= iv)
#     return base64.b64encode(iv + cipher.encrypt(raw))

# def decrypt(enc):
#     unpad = lambda s: s[:-ord(s[-1:])]

#     enc = base64.b64decode(enc)
#     iv = enc[:AES.block_size]
#     cipher = AES.new(_key_, AES.MODE_CFB, iv)
#     return unpad(base64.b64decode(cipher.decrypt(enc[AES.block_size:])).decode('utf8'))


# data  = encrypt("print(Hello World)")
# print("Data", data)

# data1  = decrypt(data)
# print("decrypt", data1)

# --------------------------------------------------------------

import os
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

_BLOCK_SIZE = 16

class AesStringCipher:
    def __init__(self, key): 
        self._key = hashlib.sha256(key.encode()).digest()

    def encrypt_str(self, raw:str) -> bytes:
        iv = os.urandom(_BLOCK_SIZE)
        cipher = Cipher(algorithms.AES(self._key), modes.CBC(iv), default_backend())
        encryptor = cipher.encryptor()
        raw = _pad(raw)
        return iv + encryptor.update(raw.encode('utf-8')) + encryptor.finalize()

    def decrypt_str(self, enc:bytes) -> str:
        iv = enc[:_BLOCK_SIZE]
        enc = enc[_BLOCK_SIZE:]
        cipher = Cipher(algorithms.AES(self._key), modes.CBC(iv), default_backend())
        decryptor = cipher.decryptor()
        raw = decryptor.update(enc) + decryptor.finalize()
        raw = raw.decode('utf-8')
        return _unpad(raw)

def _pad(s:str) -> str:
    padding = (_BLOCK_SIZE - (len(s) % _BLOCK_SIZE))
    return s + padding * chr(padding)

def _unpad(s:str) -> str:
    return s[:-ord(s[len(s)-1:])]


p1 = AesStringCipher("abdullahtayyabha")

data  = p1.encrypt_str("print(Hello World)")
print("Encypted", data)

Encypted  = p1.decrypt_str(data)
print("Decrypted", Encypted)

