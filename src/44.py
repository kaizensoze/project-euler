MAX = 2000
pent = [n*(3*n-1)/2 for n in range(1, 2*MAX)]
pdic = dict.fromkeys(pent)

def main2():
    for j in range(0, MAX):
        for k in range(j+1, 2*MAX-1):
            p_j = pent[j]
            p_k = pent[k]
            p_sum = p_j + p_k
            p_diff = p_k - p_j
            if p_sum in pdic and p_diff in pdic:
                return int(p_diff)
print(main2())
