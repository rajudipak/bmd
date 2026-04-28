n = int(input("Enter no of requests: "))
req = []

for i in range(n):
    req.append(int(input()))

head = int(input("Enter head position: "))

seek = 0
left = sorted([i for i in req if i < head])
right = sorted([i for i in req if i >= head])

print("Sequence:")
print(head, end="")

for r in right:
    seek += abs(r - head)
    head = r
    print(f" -> {head}", end="")

for r in reversed(left):
    seek += abs(r - head)
    head = r
    print(f" -> {head}", end="")

print(f"\nTotal Head Movement = {seek}")
