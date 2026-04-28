n = int(input("Enter no of requests: "))
req = []

for i in range(n):
    req.append(int(input()))

head = int(input("Enter head position: "))
seek = 0

print("Sequence:")
print(head, end="")

for r in req:
    seek += abs(r - head)
    head = r
    print(f" -> {head}", end="")

print(f"\nTotal Head Movement = {seek}")
