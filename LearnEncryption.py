# Generating Character for Encryption

import random
msg = 'Hello World'
key = ''
encryption_level = 128 // 8
char_pool = ''
for i in range(0x00, 0x255):
    char_pool += chr(i)
# print(char_pool)
# print(msg)
key = ''
for i in range(encryption_level):
    key += random.choice(char_pool)
