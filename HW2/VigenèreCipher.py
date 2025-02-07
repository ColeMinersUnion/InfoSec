from ShiftCipher import ShiftCipherEncrypt

def formatKey(plaintext: str, key: str)-> str:
    key = key.upper()
    key = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)]
    return key

def VigenèreCipherEncrypt(plaintext: str, key: str)-> str:
    ciphertext = ""
    key = formatKey(plaintext, key)
    for i, c in enumerate(plaintext):
        if c.isalpha(): #if c is a letter
            if c.isupper(): #Uppercase
                ciphertext += ShiftCipherEncrypt(c, ord(key[i])-65)
            else:           #Lowercase
                ciphertext += ShiftCipherEncrypt(c.upper(), ord(key[i])-65).lower()
        else:
            raise Exception("Invalid character in plaintext")
    return ciphertext


if __name__ == '__main__':
    #? Question 1, part A
    plain = "INFORMATION"
    key = "SECURITY"
    encrypted = VigenèreCipherEncrypt(plain, key)
    print(f"Plaintext: {plain}")
    print(f"Encrypted: {encrypted}")

