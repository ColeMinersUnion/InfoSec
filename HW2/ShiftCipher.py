def ShiftCipherEncrypt(plaintext: str, k: int)-> str:
    ciphertext = ""
    shift = [*(2*[chr(i) for i in range(65, 91)])]
    #print(shift)
    if k > 26:
        k = k % 26
    for c in plaintext:
        if c.isalpha(): #if c is a letter
            if c.isupper(): #Uppercase
                ciphertext += shift[shift.index(c)+k]
            else:           #Lowercase
                ciphertext += shift[shift.index(c.upper())+k].lower()
        else:
            raise Exception("Invalid character in plaintext")
    return ciphertext

def ShiftCipherDecrypt(ciphertext: str, k: int)-> str:
    plaintext = ""
    shift = [*(2*[chr(i) for i in range(65, 91)])]
    if k > 26:
        k = k % 26
    for c in ciphertext:
        if c.isalpha(): #if c is a letter
            if c.isupper(): #Uppercase
                plaintext += shift[shift.index(c)-k]
            else:           #Lowercase
                plaintext += shift[shift.index(c.upper())-k].lower()
        else:
            raise Exception("Invalid character in ciphertext")
    return plaintext

def CipherBreaker(ciphertext: str):
    shift = [*(2*[chr(i) for i in range(65, 91)])]
    for k in range(1, 27):
        plaintext = ""
        for c in ciphertext:
            if c.isalpha(): #if c is a letter
                if c.isupper(): #Uppercase
                    plaintext += shift[shift.index(c)-k]
                else:           #Lowercase
                    plaintext += shift[shift.index(c.upper())-k].lower()
            else:
                raise Exception("Invalid character in ciphertext")
        yield plaintext


if __name__ == '__main__':
    #? Question 1, part A
    plain = "SSOEATBENEDUMHALLOHARASTREET"
    encrypted = ShiftCipherEncrypt(plain, 5)
    decrypted = ShiftCipherDecrypt(encrypted, 5)
    
    print(f"Plaintext: {plain}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print("---------------------------------")
    print(f"Was successful: {plain == decrypted}")


    #? Question 1, part B
    print("\n---------------------------------")
    ToBeBroken = "WPXAIDEXII"
    for i, p in enumerate(CipherBreaker(ToBeBroken)):
        print(f"K {i+1}: {p}")

    #! K = 15, Plaint Text = "HAILTOPITT"
    



