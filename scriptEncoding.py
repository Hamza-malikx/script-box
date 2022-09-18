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

# val = """if not game:IsLoaded() then
# repeat wait() until game:IsLoaded()
# end
# local CoreGui = game:GetService("StarterGui") 
# CoreGui:SetCore("SendNotification", {
#  Title = "Welcome to RS Hub",
#  Text = "Checking Game",
# Duration = 5;
# })

# if game.PlaceId == 9522149469 then
# loadstring(game:HttpGet("https://raw.githubusercontent.com/MHD-444/RS-HUB/main/Strong%20Clikers"))()
# elseif game.PlaceId == 3956818381 then
# loadstring(game:HttpGet("https://raw.githubusercontent.com/MHD-444/RS-HUB/main/Ninja%20Legends"))()
# elseif game.PlaceId == 662417684 then
# loadstring(game:HttpGet("https://raw.githubusercontent.com/MHD-444/RS-HUB/main/LUCKY%20BLOCKS"))()
# elseif game.PlaceId == 8554378337 then
# loadstring(game:HttpGet("https://raw.githubusercontent.com/MHD-444/RS-HUB/main/Weapon%20Fighting%20Simulator"))()
# elseif game.PlaceId == 286090429 then
# loadstring(game:HttpGet("https://raw.githubusercontent.com/MHD-444/RS-HUB/main/Arsenal"))()
# elseif game.PlaceId == 6284583030 or game.PlaceId == 10321372166 then
# loadstring(game:HttpGet("https://raw.githubusercontent.com/MHD-444/RS-HUB/main/PSX"))()
# elseif game.PlaceId == 9498006165 then
# loadstring(game:HttpGet("https://raw.githubusercontent.com/MHD-444/RS-HUB/main/Tapping%20Simulator"))()
# elseif game.PlaceId == 3102144307 then
# loadstring(game:HttpGet("https://raw.githubusercontent.com/MHD-444/RS-HUB/main/Anime%20Clicker%20Simulator"))()
# elseif
# game.Players.LocalPlayer:Kick("this game is not supported yet.....") then
# end"""

# data  = encrypt(val)
# print("Data", data)

# data1  = decrypt(data)
# print("\n\nDecrypt", data1)

# --------------------------------------------------------------

# import os
# import hashlib
# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from cryptography.hazmat.backends import default_backend

# _BLOCK_SIZE = 16

# class AesStringCipher:
#     def __init__(self, key): 
#         self._key = hashlib.sha256(key.encode()).digest()

#     def encrypt_str(self, raw:str) -> bytes:
#         iv = os.urandom(_BLOCK_SIZE)
#         cipher = Cipher(algorithms.AES(self._key), modes.CBC(iv), default_backend())
#         encryptor = cipher.encryptor()
#         raw = _pad(raw)
#         return iv + encryptor.update(raw.encode('utf-8')) + encryptor.finalize()

#     def decrypt_str(self, enc:bytes) -> str:
#         iv = enc[:_BLOCK_SIZE]
#         enc = enc[_BLOCK_SIZE:]
#         cipher = Cipher(algorithms.AES(self._key), modes.CBC(iv), default_backend())
#         decryptor = cipher.decryptor()
#         raw = decryptor.update(enc) + decryptor.finalize()
#         raw = raw.decode('utf-8')
#         return _unpad(raw)

# def _pad(s:str) -> str:
#     padding = (_BLOCK_SIZE - (len(s) % _BLOCK_SIZE))
#     return s + padding * chr(padding)

# def _unpad(s:str) -> str:
#     return s[:-ord(s[len(s)-1:])]


# p1 = AesStringCipher("abdullahtayyabha")

# data  = p1.encrypt_str("print(Hello World)")
# print("Encypted", data)

# Encypted  = p1.decrypt_str(data)
# print("Decrypted", Encypted)


# ----------------------------------------------------------------------------

from Crypto.Cipher import AES
import base64

key = '1aec7447f7a919ef2910bd897bf869fe' # md5('You are completely crazy')
values = '{"epoc":1528711193,"temperature":28.2,"humidity":41.1,"timestamp":"2018-06-11T09:59:53","client_id":"esp8266-1458415"}'
iv = 'tARGGrNw39xRlQ4D' # length of 16 chars

print('''
Length of values : %d
key : %s
iv : %s
''' % (len(values), key, iv))

buf = values + '               '
n = len(buf) - len(buf) % 16
encoder = AES.new(key.encode(), mode=AES.MODE_CBC, IV=iv.encode())
# encoder = AES.new('This is a key123'.encode(), AES.MODE_CBC, 'This is an IV456')
data = encoder.encrypt(buf[0:n])

print('Encrypted values : ')
# print(base64.b64encode(data))
