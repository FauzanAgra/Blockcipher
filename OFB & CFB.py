from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii as ascii


print("==== PROGRAM ENKRIPSI DAN DEKRIPSI OFB dan CFB ====")
print("================= Fauzan Agra ======================")
print('===================================================\n')

tempPlaintext = bytes(input('Masukan Plaintext : '), 'utf-8')
tempKey = bytes(input('Masukan Key : '), 'utf-8')
tempIV = bytes(input('Masukan IV : '), 'utf-8')

print('\n')

plaintext = pad(tempPlaintext, AES.block_size)
key = pad(tempKey, AES.block_size)
iv = pad(tempKey, AES.block_size)


def _encryptCFB(plaintext):
    CFB = AES.new(key, AES.MODE_CFB, iv)
    hasil_enkripsi = CFB.encrypt(plaintext)
    return hasil_enkripsi


def _decryptCFB(ciphertext):
    CFB = AES.new(key, AES.MODE_CFB, iv)
    hasil_dekripsi = CFB.decrypt(ciphertext)
    Ekstrak_Bytes = unpad(hasil_dekripsi, AES.block_size)
    return Ekstrak_Bytes


def _encryptOFB(plaintext):
    ofb = AES.new(key, AES.MODE_OFB, iv)
    ciphertext = ofb.encrypt(plaintext)
    return ciphertext


def _decryptOFB(ciphertext):
    ofb = AES.new(key, AES.MODE_OFB, iv)
    hasil_decrypt = ofb.decrypt(ciphertext)
    extraced_bytes = unpad(hasil_decrypt, AES.block_size)
    return extraced_bytes


# Enkripsi & Dekripsi
ciphertext = _encryptCFB(plaintext)
print("ENKRIPSI dalam bentuk Biner : ")
print(ciphertext)
print("ENKRIPSI dalam bentuk Hexadesimal : ")
print(ascii.hexlify(ciphertext))

plaintext = _decryptCFB(ciphertext)
print("DEKRIPSI dalam bentuk Biner : ")
print(plaintext)
print("DEKRIPSI dalam bentuk ASCII : ")
print(plaintext.decode('ascii'))
