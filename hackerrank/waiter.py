def generate_primes(q):
    primes = []
    num = 2
    while len(primes) < q:
        is_prime = True
        for p in primes:
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes

def waiter(arr_p, q):
    primes = generate_primes(q)  
    answers = []

    for i in range(q):
        A, B = [], []
        prime = primes[i]

        while arr_p:
            plate = arr_p.pop()  
            if plate % prime == 0:
                B.append(plate)  
            else:
                A.append(plate)  

        answers.extend(reversed(B))
        arr_p = A 
    answers.extend(reversed(arr_p))

    return answers

if __name__ == '__main__':
    n, q = map(int, input().split())  
    arr_p = list(map(int, input().split()))  

    result = waiter(arr_p, q)  
    for i in result:
        print(i)