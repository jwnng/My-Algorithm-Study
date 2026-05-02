import itertools
import math

def is_prime(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
        
def solution(numbers):
    answer = set()
    piece = list(numbers)

    for i in range(1,len(piece)+1):
        # 순열로 primes 배열에 대입
        primes_candidates = itertools.permutations(piece,i)
        # i = 1: primes = [('1',),('7',)]
        # i = 2: primes = [('1','7'),('7','1')]
        for n in primes_candidates:
            prime_num = int("".join(n))
            
            if is_prime(prime_num):
                answer.add(prime_num)
            
    return len(answer)

# print(solution('17'))
print(solution('011'))