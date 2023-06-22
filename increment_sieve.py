def increment_sieve(n):
    candidate=3
    primes=[2]
    while len(primes)<n:
        flag=True
        for pm in primes:
            if pm**2>candidate:
                break
            elif candidate%pm==0:
                flag=False
                break
            
        if(flag):
            primes.append(candidate)
        candidate+=1
    print(primes)
increment_sieve(1000)