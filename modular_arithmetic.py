def mod_add(a, b, m):
    return (a + b) % m

def mod_sub(a, b, m):
    return (a - b) % m

def mod_mul(a, b, m):
    return (a * b) % m

def mod_exp(base, exp, m):
    return pow(base, exp, m)  # built-in fast power


a = int(input("Enter a: "))
b = int(input("Enter b: "))
m = int(input("Enter modulus m: "))

print("Modular addition:", mod_add(a, b, m))
print("Modular subtraction:", mod_sub(a, b, m))
print("Modular multiplication:", mod_mul(a, b, m))
print("Modular exponent:", mod_exp(a, b, m))
