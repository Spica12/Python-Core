def encrypt(b_obj, key):
    b_obj_array = bytearray(b_obj)

    for i, byte in enumerate(b_obj_array):

        n = byte + key

        if n > 255:
            n -= 255

        b_obj_array[i] = n

    return bytes(b_obj_array)


def decrypt(b_obj, key):
    b_obj_array = bytearray(b_obj)

    for i, byte in enumerate(b_obj_array):

        n = byte - key

        if n > 255:
            n += 255

        b_obj_array[i] = n

    return bytes(b_obj_array)



enc_pws = encrypt(b'password', 5)
print(enc_pws)

dec_pws = decrypt(enc_pws, 5)
print(dec_pws)

if __name__ == '__main__':
    pwd = input('Enter your password: ')
    pwd_bytes = pwd.encode()
    encrypt_pwd = encrypt(pwd_bytes, 200)

    with open('Modul_6_Work_with_files/3_Youtube_Theory/password.txt', 'wb') as file:
        file.write(encrypt_pwd)

    with open('Modul_6_Work_with_files/3_Youtube_Theory/password.txt', 'rb') as file:
        encrypt_pwd = file.read()
        print(encrypt_pwd)
        decrypted_pwd = decrypt(encrypt_pwd, 200)
        print(decrypted_pwd)
    


