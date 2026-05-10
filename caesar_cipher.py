def caesar_cipher(text, shift, mode='encrypt'):
    if mode == 'decrypt':
        shift = -shift
    
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    
    return ''.join(result)


text = "Hello, World!"
shift = 3

encrypted = caesar_cipher(text, shift, mode='encrypt')
decrypted = caesar_cipher(encrypted, shift, mode='decrypt')

print(f"Original:  {text}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
