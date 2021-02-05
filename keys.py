from sys import argv


def encrypt(plaintext: str) -> bytes:
    """
    Converts given plain text to cipher text using shift cipher.
    This function shifts forward every even position by 17 positions and odd ones by 21 positions.
    """

    res = []
    for p, s in enumerate(plaintext.encode('utf-8')):
        if p % 2 == 0:
            new = s + 17
        else:
            new = s + 21
        # end if
        res.append(new % 256)
    # end for
    return bytes(res)
# end def


def decrypt(ciphertext: bytes) -> str:
    """
    Converts given cipher text to plain text using shift cipher.
    This function shifts backward every even position by 17 positions and odd ones by 21 positions.
    """

    res = []
    for p, s in enumerate(ciphertext):
        if p % 2 == 0:
            new = s - 17
        else:
            new = s - 21
        # end if
        res.append(new % 256)
    # end for
    return bytes(res).decode('utf-8')
# end def


# print(argv)
if len(argv) not in [3, 4]:
    print('Usage: python keys.py -{e|d} <file> [output]')
    print('\t-e\t: encrypt\n\t-d\t: decrypt\n')
    exit(1)
# end if

file_name = argv[2]
if argv[1] == '-e':
    # read input data from file
    text = ''.join(open(file_name, 'r', encoding='utf-8').readlines())

    # get cipher code
    encrypted = encrypt(text)

    if len(argv) == 4:
        file_name = argv[3]
    else:
        # generate output filename
        file_name = file_name.rsplit(sep='.', maxsplit=1)
        if len(file_name) == 2:
            file_name = file_name[0] + '_encrypted.' + file_name[1]
        else:
            file_name = file_name[0] + '_encrypted'
        # end if
    # end if

    # write cipher code to file
    open(file_name, 'wb').write(encrypted)
    print('Encrypted data of', argv[2], ' and saved to', file_name)
elif argv[1] == '-d':
    # read input data from file
    text = b''.join(open(file_name, 'rb').readlines())

    # get plain text
    decrypted = decrypt(text)

    if len(argv) == 4:
        file_name = argv[3]
    else:
        # generate output filename
        file_name = file_name.rsplit(sep='.', maxsplit=1)
        if len(file_name) == 2:
            file_name = file_name[0] + '_decrypted.' + file_name[1]
        else:
            file_name = file_name[0] + '_decrypted'
        # end if
    # end if

    # write plain text to file
    open(file_name, 'w', encoding='utf-8').write(decrypted)
    print('Decrypted data of', argv[2], ' and saved to', file_name)
else:
    print('Usage: python keys.py -{e|d} <file> [output]')
    print('\t-e\t: encrypt\n\t-d\t: decrypt\n')
# end if
