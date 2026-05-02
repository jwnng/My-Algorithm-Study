import itertools

items = ['A','B','C','D']

# 1. 조합
print(list(itertools.combinations(items,2)))
# 2. 순열
print(list(itertools.permutations(items,3)))
# 3. 데카르트
print(list(itertools.product(['앞','뒤'],repeat=2)))
# 4. 중복 조합
print(list(itertools.combinations_with_replacement(['콜라','사이다','환타'],2)))