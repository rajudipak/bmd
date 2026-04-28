def banker_algorithm():
    
    n, r = 5, 3

    alloc = [
        [0, 0, 1],
        [3, 0, 0],
        [1, 0, 1],
        [2, 3, 2],
        [0, 0, 3]
    ]

    mx = [
        [7, 6, 3],
        [3, 2, 2],
        [8, 0, 2],
        [2, 3, 2],
        [5, 2, 3]
    ]

    avail = [2, 3, 2]

    f = [0] * n
    ans = [0] * n

    ind = 0
    done = 0

    need = [
        [mx[i][j] - alloc[i][j] for j in range(r)]
        for i in range(n)
    ]

    while done < n:

        for i in range(n):

            if not f[i] and all(need[i][j] <= avail[j] for j in range(r)):

                ans[ind] = i
                ind += 1

                for j in range(r):
                    avail[j] += alloc[i][j]

                f[i] = 1
                done += 1

    print("The SAFE Sequence is as follows")

    for i in range(n - 1):
        print(f" P{ans[i]} ->", end="")

    print(f" P{ans[n - 1]}")

banker_algorithm()
