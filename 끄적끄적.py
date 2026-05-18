# sol3)
matrix1 = [[0 for _ in range(3)] for _ in range(3)]
print(matrix1)

# sol4)
matrix2 = [[0] * 3 for _ in range(3)]
print(matrix2)

# sol5)
matrix3 = [[0] * 3] * 3
print(matrix3)

# 근데... sol5)가 가장 짧으니 저게 젤 좋을까?
# 아무 문제가 없을까?????

matrix1[0][0] = 7
print(matrix1)

matrix2[0][0] = 7
print(matrix2)

matrix3[0][0] = 7
print(matrix3)

# matrix1 = [[0 for _ in range(3)] for _ in range(3)]
# matrix2 = [[0] * 3 for _ in range(3)]
# matrix3 = [[0] * 3] * 3

# matrix3은 얕은 복사로 같은 리스트 [0 0 0]를 가리키는 포인팅 객체가
# 뿅 뿅 뿅 하고 복사됨. [객체1, 객체2, 객체3] 인데 각 객체가 
# 동일하게 저 리스트 [0 0 0]을 가리키고 있는거

# matrix2에서 [7 7 7]이 되지 않는 이유는,
# 0은 이뮤터블이라 복사가 되지 않았기 때문.
# => 이거 다시 이해.