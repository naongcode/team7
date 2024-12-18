import math
import sys
input = sys.stdin.readline

# 소수 판별 함수
def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# 입력: 갑옷의 개수 N
N = int(input())

# 갑옷 고윳값들을 저장할 리스트
armor = []
for _ in range(N):
    A = int(input())
    armor.append(A)

# 결과를 저장할 리스트
result = []

# 각 갑옷 고윳값 A에 대해 최소 변형 횟수 계산
for A in armor:
    steps = 0
    while not is_prime_number(A):  # A가 소수가 아닐 때 계속 감소
        A -= 1
        steps += 1
    result.append(steps)

# 결과 출력
for steps in result:
    print(steps)
