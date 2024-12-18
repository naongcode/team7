import sys
input = sys.stdin.readline

# 약탈할 섬의 개수
N = int(input())

# 섬 좌표들
islands = []
for i in range(N):
    x, y = map(int, input().split())
    islands.append([x, y])

# 섬들을 x 기준 오름차순, x가 같으면 y 기준 오름차순으로 정렬
sorted_island = sorted(islands, key=lambda x: (x[0], x[1]))

#sorted_island에서 각 요소의 원래 인덱스를 찾아서 매핑
original_index = {tuple(value): index for index, value in enumerate(islands)}

# 각 섬을 본거지로 삼았을 때 약탈할 수 있는 섬의 개수 계산
for j in range(N):
	base_island = islands[j]  # 본거지로 삼을 섬
	count = 0
	for i in range(N):
		# sorted_island의 섬을 기준으로 약탈할 수 있는 섬을 찾음
		if sorted_island[i][0] > base_island[0] or (sorted_island[i][0] == base_island[0] and sorted_island[i][1] > base_island[1]):
			count += 1
	print(count)
