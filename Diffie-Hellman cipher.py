def calculate_shared_key(p, g, private_key):
    public_key = (g ** private_key) % p
    return public_key

def calculate_shared_secret_key(p, public_key, private_key):
    shared_secret_key = (public_key ** private_key) % p
    return shared_secret_key

# Входные параметры
p = int(input("Введите простое число p: "))
g = int(input("Введите число g: "))
private_key_A = int(input("Введите секретный ключ для A: "))
private_key_B = int(input("Введите секретный ключ для B: "))

# Вычисление открытых ключей для обоих сторон
public_key_A = calculate_shared_key(p, g, private_key_A)
public_key_B = calculate_shared_key(p, g, private_key_B)

# Вычисление общего секретного ключа для обоих сторон
shared_secret_key_A = calculate_shared_secret_key(p, public_key_B, private_key_A)
shared_secret_key_B = calculate_shared_secret_key(p, public_key_A, private_key_B)

print("Общий секретный ключ для A:", shared_secret_key_A)
print("Общий секретный ключ для B:", shared_secret_key_B)

