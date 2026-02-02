class RingZn:
    def __init__(self, n):
        self.n = n

    def add(self, a, b):
        return (a + b) % self.n

    def mul(self, a, b):
        return (a * b) % self.n


n = int(input("Enter n: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))

ring = RingZn(n)
print("Ring addition:", ring.add(a, b))
print("Ring multiplication:", ring.mul(a, b))
