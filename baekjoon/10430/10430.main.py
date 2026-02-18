a, b, c = [int(x) for x in input().split(" ")]
print((a + b) % c)
print((a % c + b % c) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)
