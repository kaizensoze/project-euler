from ProjectEulerLibrary import lcm

# assume a and b are (num, denom) tuples
def fadd(a, b):
    a_num = a[0]
    a_den = a[1]
    b_num = b[0]
    b_den = b[1]
    z = lcm(a_den, b_den)
    if a_den != z:
        a_num *= z
    if b_den != z:
        b_num *= z
    return (a_num+b_num, z)

# assume a and b are (num, denom) tuples
def fdiv(a, b):
    a_num = a[0]
    a_den = a[1]
    b_num = b[0]
    b_den = b[1]
    return (a_num*b_den, a_den*b_num)

def operate(n):
    return fdiv((1,1), fadd(n, (2,1)))

count = 0
stored = [(1,2)]
for i in range(1, 1000+1):
    new_val = operate(stored[i-1])
    stored.append(new_val)
    result = fadd(new_val, (1,1))
    #print(result)
    result_num_size = len(str(result[0]))
    #print(result_num_size)
    result_den_size = len(str(result[1]))
    #print(result_den_size)
    if result_num_size > result_den_size:
        count += 1
print(count)
