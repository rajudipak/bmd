p=['P1','P2','P3']
at=[0,0,0]
bt=[10,5,8]
pr=[2,1,3]

n=len(p)

ct=[0]*n
tat=[0]*n
wt=[0]*n
done=[0]*n

t=0

for _ in range(n):
    idx=-1
    mn=999

    for i in range(n):
        if not done[i] and pr[i]<mn:
            mn=pr[i]
            idx=i

    t+=bt[idx]
    ct[idx]=t
    done[idx]=1

for i in range(n):
    tat[i]=ct[i]-at[i]
    wt[i]=tat[i]-bt[i]

print(f"{'P':<5}{'AT':<5}{'BT':<5}{'PR':<5}{'CT':<5}{'TAT':<6}{'WT'}")
for i in range(n):
    print(f"{p[i]:<5}{at[i]:<5}{bt[i]:<5}{pr[i]:<5}{ct[i]:<5}{tat[i]:<6}{wt[i]}")
