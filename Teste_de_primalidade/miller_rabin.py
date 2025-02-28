import random

def miller_rabin(n, k=5):
    # Retorna True se n é provável que seja primo, e False se é composto
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
        
    if n==2 or n==3 or n==5 or n==7:
        return True 

    # Escreve n-1 como 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Testes de base
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # x = (a^d) % n

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)  # x = (x^2) % n
            if x == n - 1:
                break
        else:
            return False

    return True

