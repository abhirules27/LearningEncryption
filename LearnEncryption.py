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
#print(key)

key_index = 0
max_key_index = encryption_level - 1
encrypted_msg = ''
for char in msg:
    encrypted_char = ord(char) ^ ord(key[key_index])
    encrypted_msg += chr(encrypted_char)

    # Checking Index Status
    if key_index >= max_key_index:
        key_index = 0
    else:
        key_index += 1
print(msg)
print(encrypted_msg)