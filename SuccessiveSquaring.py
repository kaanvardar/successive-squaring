from math import pow

def successiveSquaring(base,exponent,mod):
    b = 1

    while mod >= 1:
        if (mod % 2 == 1):
            b = base * b % mod
            base = pow(base,2) % mod
            mod = mod / 2
        return b

#main
result = successiveSquaring(28,749,1147)
print(result)