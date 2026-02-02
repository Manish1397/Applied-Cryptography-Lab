def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
class FieldZp:
    def __init__(self, p):
        if not is_prime(p):
            raise ValueError("p must be prime")
        self.p = p
    def add(self, a, b):
        return (a + b) % self.p
    def mul(self, a, b):
        return (a * b) % self.p
    def inverse(self, a):
        return pow(a, self.p - 2, self.p)
    def div(self, a, b):
        return self.mul(a, self.inverse(b))
p = int(input("Enter prime p: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))
field = FieldZp(p)
print("Field addition:", field.add(a, b))
print("Field multiplication:", field.mul(a, b))
print("Field division:", field.div(a, b))