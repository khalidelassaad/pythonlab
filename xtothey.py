def xtothey(x, y, p):
    Memo = [x % p]  # Memo[i] = x**(2**i)mod p
    factor = []


    powerof2 = 1
    runningproduct = 1
    while y != 0:
        # grab the last bit and if 1 save it in memo properly
        Memo.append( ( (Memo[powerof2 - 1] % p) * (Memo[powerof2 - 1] % p)  ) %  p)
        if y & 1:
            runningproduct = (runningproduct * Memo[powerof2-1]) % p
            factor.append(Memo[powerof2-1])
        y >>= 1
        powerof2 += 1
    print(Memo)
    print(factor)
    return runningproduct

print(xtothey(97,3343,2015))