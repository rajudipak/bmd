p=['P1','P2','P3']
at=[0,0,0]
bt=[10,5,8]

q=2
n=len(p)

rt=bt[:]
ct=[0]*n
tat=[0]*n
wt=[0]*n

t=0

while sum(rt)>0:
    for i in range(n):
        if rt[i]>0:
            x=min(q,rt[i])
            t+=x
            rt[i]-=x
            if rt[i]==0:
                ct[i]=t

for i in range(n):
    tat[i]=ct[i]-at[i]
    wt[i]=tat[i]-bt[i]

print(f"{'P':<5}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<6}{'WT'}")
for i in range(n):
    print(f"{p[i]:<5}{at[i]:<5}{bt[i]:<5}{ct[i]:<5}{tat[i]:<6}{wt[i]}")
