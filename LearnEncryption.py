# Generating Character for Encryption

import random
msg = 'Hello World. How are you doing!'

# Stage 1: Generating Key

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

# Stage 2: Checking for Msg len vs Key len Cycle

key_index = 0                           # Current Cycle
max_key_index = encryption_level - 1    # 15th Cycle
encrypted_msg = ''                      # Blank Encrypted Msg
for char in msg:
    encrypted_char = ord(char) ^ ord(key[key_index])    # Ord converts Char to ASCII
    encrypted_msg += chr(encrypted_char)

    # Checking Index Status
    if key_index >= max_key_index:
        key_index = 0
    else:
        key_index += 1
print(f'\nOriginal Message : {msg}')
print(f'Encrypted Message: {encrypted_msg}')

# Stage 3: Decrypting Message
key_index = 0
decrypted_msg = ''
for char in encrypted_msg:
    decrypted_char = ord(char) ^ ord(key[key_index])
    decrypted_msg += chr(decrypted_char)

    # Checking Index Status
    if key_index >= max_key_index:
        key_index = 0
    else:
        key_index += 1
print(f'Decrypted Message: {decrypted_msg}')