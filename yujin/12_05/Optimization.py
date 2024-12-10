import numpy as np
length,min_height,location = map(int,input().split())
location-=1
tree = np.array(input().split(), dtype=int)
Q = int(input())
direction = input().split()

#벌목한 횟수를 저장할 변수
amount = 0

for i in range(Q):
    #벌목 할 수 있는 조건 충족(min_height보다 크거나 같을 때)
	if (tree[location] >= min_height):
		# 벌목하기
		amount+=tree[location]
		tree[location] = 0
	#이동하기
	if (direction[i] == 'R'):
		location = (location + 1) % length
	elif (direction[i] == 'L'):
		location = (location-1) % length
	# 자라기
	tree+=1
print(amount)