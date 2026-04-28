p = ['P1', 'P2', 'P3', 'P4', 'P5']
at = [0, 2, 6, 7, 13]
bt = [4, 16, 12, 8, 2]

n = len(p)

ct = [0] * n
tat = [0] * n
wt = [0] * n

ct[0] = at[0] + bt[0]

for i in range(1, n):
    ct[i] = max(ct[i - 1], at[i]) + bt[i]

for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

print(f"{'P':<5}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<6}{'WT'}")

for i in range(n):
    print(f"{p[i]:<5}{at[i]:<5}{bt[i]:<5}{ct[i]:<5}{tat[i]:<6}{wt[i]}")

print("\nAverage TAT =", sum(tat) / n)
print("Average WT =", sum(wt) / n)
