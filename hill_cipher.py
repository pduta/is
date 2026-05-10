import numpy as np

def mod_inverse(a, m=26):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_mod_inverse(matrix, mod=26):
    det = int(round(np.linalg.det(matrix))) % mod
    det_inv = mod_inverse(det % mod, mod)
    if det_inv is None:
        raise ValueError(f"Matrix is not invertible mod 26 (det mod 26 = {det})")
    size = matrix.shape[0]
    if size == 2:
        adj = np.array([
            [ matrix[1,1], -matrix[0,1]],
            [-matrix[1,0],  matrix[0,0]]
        ])
    else:
        cofactors = np.zeros_like(matrix)
        for r in range(size):
            for c in range(size):
                minor = np.delete(np.delete(matrix, r, axis=0), c, axis=1)
                cofactors[r,c] = ((-1)**(r+c)) * round(np.linalg.det(minor))
        adj = cofactors.T
    inv = (det_inv * adj) % mod
    return inv.astype(int)

def prepare_text(text, block_size):
    text = text.upper()
    filtered = [ch for ch in text if ch.isalpha()]
    while len(filtered) % block_size != 0:
        filtered.append('X')
    return filtered

def hill_encrypt(text, key_matrix):
    n = key_matrix.shape[0]
    chars = prepare_text(text, n)
    result = []
    for i in range(0, len(chars), n):
        block = np.array([ord(ch) - ord('A') for ch in chars[i:i+n]])
        encrypted = (key_matrix @ block) % 26
        result += [chr(v + ord('A')) for v in encrypted]
    return ''.join(result)

def hill_decrypt(text, key_matrix):
    n = key_matrix.shape[0]
    inv_key = matrix_mod_inverse(key_matrix)
    chars = [ch for ch in text.upper() if ch.isalpha()]
    result = []
    for i in range(0, len(chars), n):
        block = np.array([ord(ch) - ord('A') for ch in chars[i:i+n]])
        decrypted = (inv_key @ block) % 26
        result += [chr(int(v) + ord('A')) for v in decrypted]
    return ''.join(result)

def validate_key(matrix):
    det = int(round(np.linalg.det(matrix))) % 26
    inv = mod_inverse(det, 26)
    print(f"  det mod 26 = {det}, modular inverse = {inv} → {'VALID' if inv else 'INVALID'}")

def print_matrix(matrix, label):
    print(f"\n{label}:")
    for row in matrix:
        print("  " + "  ".join(f"{v:3}" for v in row))


key_2x2 = np.array([[3, 2], [7, 5]])
key_3x3 = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
text = "Hello World"

print("=" * 45)
print("HILL CIPHER — 2×2 KEY")
print("=" * 45)
validate_key(key_2x2)
print(f"Original:  {text}")
enc2 = hill_encrypt(text, key_2x2)
dec2 = hill_decrypt(enc2, key_2x2)
print(f"Encrypted: {enc2}")
print(f"Decrypted: {dec2}")
print_matrix(key_2x2, "Key Matrix")
print_matrix(matrix_mod_inverse(key_2x2), "Inverse Key Matrix (mod 26)")

print("\n" + "=" * 45)
print("HILL CIPHER — 3×3 KEY")
print("=" * 45)
validate_key(key_3x3)
print(f"Original:  {text}")
enc3 = hill_encrypt(text, key_3x3)
dec3 = hill_decrypt(enc3, key_3x3)
print(f"Encrypted: {enc3}")
print(f"Decrypted: {dec3}")
print_matrix(key_3x3, "Key Matrix")
print_matrix(matrix_mod_inverse(key_3x3), "Inverse Key Matrix (mod 26)")
