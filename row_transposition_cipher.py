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

    col_lengths = [rows] * n
    columns = {}
    idx = 0
    for col in order:
        columns[col] = list(ciphertext[idx:idx+col_lengths[col]])
        idx += col_lengths[col]

    plaintext = ''
    for r in range(rows):
        for c in range(n):
            plaintext += columns[c][r]
    return plaintext


def print_grid(text, key):
    n = len(key)
    while len(text) % n != 0:
        text += 'X'
    rows = [text[i:i+n] for i in range(0, len(text), n)]
    order = sorted(range(n), key=lambda i: key[i])
    rank = [0] * n
    for rank_val, col in enumerate(order):
        rank[col] = rank_val + 1

    print("  Key:  ", ' '.join(str(k) for k in key))
    print("  Order:", ' '.join(str(r) for r in rank))
    print("  " + "-" * (n * 2 + 1))
    for row in rows:
        print("  |" + '|'.join(row) + '|')
    print("  " + "-" * (n * 2 + 1))


key = [3, 1, 4, 2]
text = "Hello World"

encrypted = row_transposition_encrypt(text, key)
decrypted = row_transposition_decrypt(encrypted, key)

print("=" * 45)
print("ROW TRANSPOSITION CIPHER")
print("=" * 45)
print(f"\nKey:       {key}")
print(f"Original:  {text}")
print()
print("Grid:")
print_grid(text.replace(" ", "").upper(), key)
print()
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
