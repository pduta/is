def prepare_key_matrix(key):
    key = key.upper().replace("J", "I")
    seen = []
    for ch in key:
        if ch.isalpha() and ch not in seen:
            seen.append(ch)
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in seen:
            seen.append(ch)
    return [seen[i*5:(i+1)*5] for i in range(5)]


def get_position(matrix, char):
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)


def prepare_text(text):
    text = text.upper().replace("J", "I")
    filtered = [ch for ch in text if ch.isalpha()]
    pairs = []
    i = 0
    while i < len(filtered):
        a = filtered[i]
        b = filtered[i+1] if i+1 < len(filtered) else 'X'
        if a == b:
            pairs.append((a, 'X'))
            i += 1
        else:
            pairs.append((a, b))
            i += 2
    return pairs


def playfair_encrypt(text, key):
    matrix = prepare_key_matrix(key)
    pairs = prepare_text(text)
    result = []
    for a, b in pairs:
        r1, c1 = get_position(matrix, a)
        r2, c2 = get_position(matrix, b)
        if r1 == r2:
            result += [matrix[r1][(c1+1)%5], matrix[r2][(c2+1)%5]]
        elif c1 == c2:
            result += [matrix[(r1+1)%5][c1], matrix[(r2+1)%5][c2]]
        else:
            result += [matrix[r1][c2], matrix[r2][c1]]
    return ''.join(result)


def playfair_decrypt(text, key):
    matrix = prepare_key_matrix(key)
    text = text.upper()
    pairs = [(text[i], text[i+1]) for i in range(0, len(text), 2)]
    result = []
    for a, b in pairs:
        r1, c1 = get_position(matrix, a)
        r2, c2 = get_position(matrix, b)
        if r1 == r2:
            result += [matrix[r1][(c1-1)%5], matrix[r2][(c2-1)%5]]
        elif c1 == c2:
            result += [matrix[(r1-1)%5][c1], matrix[(r2-1)%5][c2]]
        else:
            result += [matrix[r1][c2], matrix[r2][c1]]
    return ''.join(result)


def print_matrix(matrix):
    print("  " + " ".join(f"{i}" for i in range(5)))
    for i, row in enumerate(matrix):
        print(f"{i} " + " ".join(row))


key = "MONARCHY"
text = "Hello World"

matrix = prepare_key_matrix(key)
encrypted = playfair_encrypt(text, key)
decrypted = playfair_decrypt(encrypted, key)

print("=" * 40)
print("PLAYFAIR CIPHER")
print("=" * 40)
print(f"\nKey:       {key}")
print(f"Original:  {text}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
print("\nKey Matrix:")
print_matrix(matrix)
