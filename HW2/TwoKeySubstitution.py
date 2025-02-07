def TwoKeySubstitutionEncrypt(plaintext: str, key1: list, key2: list)->str:
    ciphertext = ""
    for i, c in enumerate(plaintext):
        if i % 2 == 0:
            ciphertext += CharSub(c, key1)
        else:
            ciphertext += CharSub(c, key2)
    return ciphertext

def CharSub(c: str, key: list)->chr:
    return key[ord(c)-65]

def generate_key()->list:
    from random import sample, seed
    from time import time
    seed(time())
    return sample([chr(i) for i in range(65, 91)], 26)

def TwoKeySubstitutionDecrypt(ciphertext: str, key1: list, key2: list)->str:
    plaintext = ""
    for i, c in enumerate(ciphertext):
        if c == ' ':
            continue
        if i % 2 == 0:
            plaintext += chr(65 + key1.index(c))
        else:
            plaintext += chr(65 + key2.index(c))
    return plaintext

if __name__ == '__main__':
    #key1 = generate_key()
    #key2 = generate_key()
    key1 = ['C', 'V', 'B', 'J', 'M', 'A', 'S', 'D', 'F', 'G', 'H', 'L', 'K', 'N', 'W', 'Q', 'R', 'T', 'E', 'Z', 'P', 'U', 'I', 'O', 'Y', 'X']
    key2 = ['D', 'G', 'J', 'L', 'A', 'Q', 'E', 'T', 'Z', 'C', 'B', 'U', 'O', 'M', 'P', 'K', 'N', 'V', 'X', 'I', 'H', 'Y', 'R', 'W', 'F', 'S']
    #? I removed a space because it was not in the key, and I did not want to deal with it
    plaintext = ["INFORMATION", "TOPIC", 'INFORMATIONTOPIC']
    print(f"Key 1: {key1}")
    print(f"Key 2: {key2}")
    for p in plaintext:
        encrypted = TwoKeySubstitutionEncrypt(p, key1, key2)
        print(f"Plaintext: {p}")
        print(f"Encrypted: {encrypted}")
    
    ciphertext = ["NAZRWVHXMJPVFIY", "NAZRWVHX", " XMJPVFIY"]
    for c in ciphertext:
        decrypted = TwoKeySubstitutionDecrypt(c, key1, key2)
        print(f"Ciphertext: {c}")
        print(f"Decrypted: {decrypted}")
    