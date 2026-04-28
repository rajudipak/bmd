p=['P1','P2','P3','P4','P5']
at=[0,2,6,7,13]
bt=[4,16,12,8,2]

n=len(p)
rt=bt[:]
ct=[0]*n
tat=[0]*n
wt=[0]*n

t=done=0

while done<n:
    idx=-1
    mn=999

    for i in range(n):
        if at[i]<=t and rt[i]>0 and rt[i]<mn:
            mn=rt[i]
            idx=i

    if idx==-1:
        t+=1
        continue

    rt[idx]-=1
    t+=1

    if rt[idx]==0:
        ct[idx]=t
        done+=1

for i in range(n):
    tat[i]=ct[i]-at[i]
    wt[i]=tat[i]-bt[i]

print(f"{'P':<5}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<6}{'WT'}")
for i in range(n):
    print(f"{p[i]:<5}{at[i]:<5}{bt[i]:<5}{ct[i]:<5}{tat[i]:<6}{wt[i]}")
