def rail_fence_encrypt(text, rails):
    fence = [[] for _ in range(rails)]
    rail, direction = 0, 1
    for char in text:
        fence[rail].append(char)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction
    return ''.join(''.join(r) for r in fence)


def rail_fence_decrypt(text, rails):
    n = len(text)
    pattern = []
    rail, direction = 0, 1
    for i in range(n):
        pattern.append(rail)
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        rail += direction

    indices = sorted(range(n), key=lambda i: pattern[i])
    result = [''] * n
    for i, char in zip(indices, text):
        result[i] = char
    return ''.join(result)


text = "Hello World"
for rails in [2, 3, 4]:
    encrypted = rail_fence_encrypt(text, rails)
    decrypted = rail_fence_decrypt(encrypted, rails)
    print(f"Rails: {rails}")
    print(f"  Original:  {text}")
    print(f"  Encrypted: {encrypted}")
    print(f"  Decrypted: {decrypted}")
