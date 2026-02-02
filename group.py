class MultiplicativeGroup:
    def __init__(self, n):
        self.n = n

    def operation(self, a, b):
        return (a * b) % self.n


n = int(input("Enter n: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))

group = MultiplicativeGroup(n)
print("Group operation result:", group.operation(a, b))
