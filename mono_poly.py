import random
import string


def generate_monoalphabetic_key():
    alphabet = list(string.ascii_lowercase)
    shuffled = alphabet.copy()
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))


def monoalphabetic_encrypt(text, key):
    result = []
    for char in text:
        if char.islower():
            result.append(key[char])
        elif char.isupper():
            result.append(key[char.lower()].upper())
        else:
            result.append(char)
    return ''.join(result)


def monoalphabetic_decrypt(text, key):
    reverse_key = {v: k for k, v in key.items()}
    result = []
    for char in text:
        if char.islower():
            result.append(reverse_key[char])
        elif char.isupper():
            result.append(reverse_key[char.lower()].upper())
        else:
            result.append(char)
    return ''.join(result)


def vigenere_encrypt(text, keyword):
    keyword = keyword.lower()
    result = []
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(keyword[key_index % len(keyword)]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)


def vigenere_decrypt(text, keyword):
    keyword = keyword.lower()
    result = []
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(keyword[key_index % len(keyword)]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)


text = "Hello, World!"
keyword = "secret"

print("=" * 45)
print("MONOALPHABETIC CIPHER")
print("=" * 45)
mono_key = generate_monoalphabetic_key()
mono_encrypted = monoalphabetic_encrypt(text, mono_key)
mono_decrypted = monoalphabetic_decrypt(mono_encrypted, mono_key)
print(f"Original:  {text}")
print(f"Encrypted: {mono_encrypted}")
print(f"Decrypted: {mono_decrypted}")

print()
print("=" * 45)
print("POLYALPHABETIC CIPHER (Vigenere)")
print("=" * 45)
poly_encrypted = vigenere_encrypt(text, keyword)
poly_decrypted = vigenere_decrypt(poly_encrypted, keyword)
print(f"Original:  {text}")
print(f"Keyword:   {keyword}")
print(f"Encrypted: {poly_encrypted}")
print(f"Decrypted: {poly_decrypted}")
