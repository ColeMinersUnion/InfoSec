def generate_random_substitution_table()->dict:
    keys = [chr(c) for c in range(65, 91)] # A-Z
    possible_values = [chr(c) for c in range(33, 127)]
    from random import choice
    values = [choice(possible_values) for _ in range(26)] 
    return dict(zip(keys, values))

def RandomSubstitutionCipherEncrypt(plaintext: str, table: dict)-> str:
    ciphertext = ""
    for c in plaintext:
        if c.isalpha(): #if c is a letter
            if c.isupper(): #Uppercase
                ciphertext += table[c]
            else:           #Lowercase
                ciphertext += table[c.upper()].lower()
        else:
            raise Exception("Invalid character in plaintext")
    return ciphertext

def RandomSubstitutionCipherDecrypt(ciphertext: str, table: dict)-> list:
    #! In the example table, two characters can be mapped to the same character
    #! Therefore, decryption is not unique, and a list of possible plaintexts is returned
    #* The decryption table is the inverse of the encryption table

    if len(set(table.values())) != 26:
        from copy import deepcopy
        #* If there are duplicate values in the table, decryption is not unique
        possible_plaintexts = []
        decryption_tables = [{}]
        current_table = 0
        print(f'\nDuplicate (Encoded Character: Possible Plain characters) {Duplicates(table)}\n')
        for k, v in table.items():
            if v not in decryption_tables[0].keys():
                for table in decryption_tables:
                    table[v] = k
            else:
                current_table += 1
                decryption_tables.append(deepcopy(decryption_tables[0]))
                decryption_tables[current_table][v] = k
        for table in decryption_tables:
            possible_plaintexts.append(Decrypt(ciphertext, table))
        return possible_plaintexts

        
    else:
        return [Decrypt(ciphertext, {v: k for k, v in table.items()})]
    
        
def Decrypt(ciphertext: str, decryption_table: dict)-> str:       
        plaintext = ""
        for c in ciphertext:
            if c in decryption_table.keys():
                plaintext += decryption_table[c]
            else:
                raise Exception("Invalid character in ciphertext")
        return plaintext

def Duplicates(table: dict)->dict:
    duplicates = {}
    for k, v in table.items():
        if v not in duplicates.keys():
            duplicates[v] = [k]
        else:
            duplicates[v].append(k)
    duplicates = {k: v for k, v in duplicates.items() if len(v) > 1}
    return duplicates

        


if __name__ == '__main__':
    table = generate_random_substitution_table()
    print(table)
    #? Question 2, part A
    plain = "PENNSYLVANIA"
    encrypted = RandomSubstitutionCipherEncrypt(plain, table)
    decrypted_options = RandomSubstitutionCipherDecrypt(encrypted, table)
    print(f"Plaintext: {plain}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted_options}")
    print("---------------------------------")
    print(f"Was successful: {plain in decrypted_options}")

