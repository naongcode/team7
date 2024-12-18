n, k = map(int, input().split())
a = []
for i in range(n):
	b = list(map(int, input().split()))
	a.append(b)
# print(a, "\n")

# # 1의 개수 찾기
# indices = [ 
# 	(row_index, col_index) 
# 	for row_index, row in enumerate(a) 
# 	for col_index, value in enumerate(row) 
# 	if value == 1]
# print (indices)


# 인접8칸 탐색함수 작성하기
# 탐색좌표가 음수이면 미실행
find_list = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
def finding(row, col, grid):
	count = 0
	for dx,dy in find_list: #8방향의 좌표를 더해주기
		new_row = row + dy
		new_col = col + dx
		
		#경계 벗어나지 않게
		if new_row >=0 and new_col >=0 and new_row < n and new_col <n:
			if grid[new_row][new_col]==1:
				count += 1
	return count

# 0값인 좌표에서 탐색 실행
# 주어진 k값과 같으면 카운팅
result = 0
for p in range(n):
	for q in range(n):
		if a[p][q]==0:
			if finding(p, q, a)==k:
				result +=1
				
print(result)