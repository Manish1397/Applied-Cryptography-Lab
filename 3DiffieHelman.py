import random

p = 23
g = 5

a = random.randint(1, p-2)
b = random.randint(1, p-2)

A = pow(g, a, p)
B = pow(g, b, p)

key_A = pow(B, a, p)
key_B = pow(A, b, p)

print("Public prime (p):", p)
print("Primitive root (g):", g)

print("\nAlice private key:", a)
print("Bob private key:", b)

print("\nAlice public key:", A)
print("Bob public key:", B)

print("\nShared key (Alice):", key_A)
print("Shared key (Bob):", key_B)
