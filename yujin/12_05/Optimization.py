import numpy as np
length,min_height,location = map(int,input().split())
location-=1
tree = np.array(input().split(), dtype=int)
Q = int(input())
direction = input().split()

#벌목한 횟수를 저장할 변수
amount = 0
growth = 0
for i in range(Q):
    # 벌목 조건 확인
    if (tree[location] + growth >= min_height):
        amount += tree[location] + growth
        tree[location] = 0  # 벌목 후 나무 값 0으로 설정
    # 방향 이동
    if direction[i] == 'R':
        location = (location + 1) % length
    elif direction[i] == 'L':
        location = (location - 1) % length
    # 성장 값 증가
    growth += 1
	
print(amount)
