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


text = input('Give text: ')
e = encrypt(text)
print('Encrypted:', e)
d = decrypt(e)
print('Decrypted:', d)
