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
    if (tree[location] + growth >= min_height):
        amount += tree[location] + growth
        tree[location] = -growth  # 벌목한 나무는 현재 성장을 기준으로 초기화
    if direction[i] == 'R':
        location = (location + 1) % length
    elif direction[i] == 'L':
        location = (location - 1) % length
    growth += 1
	
print(amount)
