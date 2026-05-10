def substitution_encrypt(text, shift=3):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)


def substitution_decrypt(text, shift=3):
    return substitution_encrypt(text, -shift)


def row_transposition_encrypt(text, key):
    text = text.replace(" ", "").upper()
    n = len(key)
    while len(text) % n != 0:
        text += 'X'
    rows = [text[i:i+n] for i in range(0, len(text), n)]
    order = sorted(range(n), key=lambda i: key[i])
    return ''.join(''.join(row[i] for row in rows) for i in order)


def row_transposition_decrypt(ciphertext, key):
    n = len(key)
    rows = len(ciphertext) // n
    order = sorted(range(n), key=lambda i: key[i])
    columns = {}
    idx = 0
    for col in order:
        columns[col] = list(ciphertext[idx:idx+rows])
        idx += rows
    plaintext = ''
    for r in range(rows):
        for c in range(n):
            plaintext += columns[c][r]
    return plaintext


def product_encrypt(text, shift, key):
    after_sub = substitution_encrypt(text, shift)
    after_trans = row_transposition_encrypt(after_sub, key)
    return after_trans


def product_decrypt(ciphertext, shift, key):
    after_trans = row_transposition_decrypt(ciphertext, key)
    after_sub = substitution_decrypt(after_trans, shift)
    return after_sub


def print_stage(label, text):
    print(f"  {label:<22} {text}")


shift = 3
key = [3, 1, 4, 2]
text = "Hello World"

after_sub = substitution_encrypt(text, shift)
after_trans = row_transposition_encrypt(after_sub, key)
after_trans2 = row_transposition_decrypt(after_trans, key)
after_sub2 = substitution_decrypt(after_trans2, shift)

encrypted = product_encrypt(text, shift, key)
decrypted = product_decrypt(encrypted, shift, key)

print("=" * 50)
print("PRODUCT CIPHER")
print("=" * 50)
print(f"\nShift Key:        {shift}")
print(f"Transposition Key: {key}")
print()
print("ENCRYPTION STAGES:")
print_stage("Plaintext:", text)
print_stage("After Substitution:", after_sub)
print_stage("After Transposition:", after_trans)
print()
print("DECRYPTION STAGES:")
print_stage("Ciphertext:", encrypted)
print_stage("After Reverse Trans:", after_trans2)
print_stage("After Reverse Sub:", after_sub2)
print()
print(f"Final Encrypted: {encrypted}")
print(f"Final Decrypted: {decrypted}")
