import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from sys import argv
import sys
import math
'''======================================================================
to do: choose a random key
output: bytes type; 16 bytes
======================================================================'''


def gen(bin_file):
    key_file = open(bin_file, 'wb')
    new_key = get_random_bytes(16)
    key_file.write(new_key)
    key_file.close()
    return new_key


'''======================================================================
to do: add a padding to ensure the length of the padded data is
        a multiple of 16
input: bytes type
output: bytes type.
WARNING: CAREFULLY READ THE NOTES and figure out what to do
======================================================================'''


def add_padding(data):
    message = data
    if len(data) % 16 == 0:
        padded_msg = bytearray()
        for i in range(16):
            padded_msg.append(16)
        return data + padded_msg
    else:
        get_pad_len = 16 - len(message) % 16
        padded_msg = bytearray()
        for i in range(get_pad_len):
            padded_msg.append(get_pad_len)
        message += padded_msg
        return message


'''======================================================================
to do: remove the padding and return the original data before padding.
       do the reverse of add_padding
    1. see if the length of the input data is a mutiple of 16
    2. see if the padding is correct IN EVERY BYTE of the padding
    3. if everything is good, then take out the padding
input: bytes type
output: m, b
    m: bytes type.
    b: True/False.
======================================================================'''


def remove_padding(data):

    padding_num = 0
    message = data
    answer = bytearray(message)
    false_answer = bytearray()
    if len(message) % 16 == 0:
        i = len(message) - 16
        while i < (len(message)):
            if message[i] in range(0, 17):
                if message[i] == message[i + 1]:
                    padding_num = len(message) - message[i]
                    answer = answer[0:padding_num]
                    return answer, True
                else:

                    return answer, False
            i += 1
    else:
        return answer, False


'''======================================================================
to do: implement CBC encryption.
    1. Create AES object aes using AES.new
       You should give (key, mode, iv) CORRECTLY when you call AES.new
    2. Call add_padding you implemented above to pad the message m
    3. Call aes.encrypt by giving the padded message as an argument
input:
    k: bytes type, must be 16 bytes
    iv: bytes type, must be 16 bytes
    m: bytes type, any arbitrary-length message.
output:
    bytes: ciphertext encrypted with CBC mode
======================================================================'''


def encrypt_basic(k, iv, m):
    aes = AES.new(k, AES.MODE_ECB)
    IV = iv
    counter = math.ceil(len(m) / 16)
    answer = bytearray()
    for ct in range(counter):
        start = ct * 16
        end = (ct + 1) * 16
        plaintext = m[start:end]
        if len(plaintext) == 16:
            padded_msg = plaintext
        else:
            padded_msg = add_padding(plaintext)
        ciphertextArray = bytearray(len(padded_msg))
        for i in range(len(padded_msg)):
            ciphertextArray[i] = (iv[i] ^ padded_msg[i])
        ciphertext = ciphertextArray
        ciphertext = aes.encrypt(ciphertext)
        answer += ciphertext
        if ct == counter - 1:
            return IV + answer
        iv = ciphertext


'''======================================================================
to do: implement CBC decryption.
    1. Create AES object aes using AES.new
       You should give (key, iv, mode) CORRECTLY when you call AES.new
    2. Call aes.decrypt on the given ciphertext
    2. Call remove_padding you implemented above to extract the original message m
input:
    k: bytes type, must be 16 bytes
    iv: bytes type, must be 16 bytes
    c: bytes type, any arbitrary-length ciphertext.
output: m
    m: bytes type - plaintext decrypted with CBC mode
        return an empty bytes object if an error occurs
======================================================================'''


def decrypt_basic(k, iv, c):
    aes = AES.new(k, AES.MODE_ECB)
    finalIV = iv
    count = math.ceil(len(c) / 16)
    answer = []
    for i in range(count):
        answer.append(None)
    while count > 0:
        end = count * 16
        cipher = end - 16
        IV = cipher - 16
        if IV < 0:
            iv = finalIV
        else:
            iv = c[IV:cipher]
        plaintext = bytearray(aes.decrypt(c[cipher:end]))
        plaintextArray = bytearray(len(plaintext))
        for i in range(len(plaintext)):
            plaintextArray[i] = (iv[i] ^ plaintext[i])
        if ((plaintextArray[15])) < 17:
            unpad, bol = remove_padding((plaintextArray))
        else:
            unpad = plaintextArray
        answer[count - 1] = unpad
        count -= 1
    order = len(answer)
    plaintext = bytearray()
    for i in range(order):
        plaintext += answer[i]
    return bytes(plaintext)

def encrypt(k, m):
    iv = get_random_bytes(16)
    c = encrypt_basic(k, iv, m)
    return c


'''======================================================================
to do: implement full CBC decryption.
    1. Given c, extract iv and the rest c0
    2. call decrypt_basic to decrypt c0
input:
    k: bytes type, must be 16 bytes
    c: bytes type, any arbitrary-length ciphertext.
        Remember the full ciphertext c is really iv + c0
output: m
    m: bytes type - plaintext decrypted with CBC mode
        return an empty bytes object if an error occurs
======================================================================'''


def decrypt(k, c):
    iv = c[:16]
    dec = decrypt_basic(k, iv, c[16:])
    return dec
