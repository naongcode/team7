n, m ,k = map(int, input().split())

l_x = []
l_y = []
for i in range(k):
	y, x = list(map(int,input().split()))
	l_x.append(x)
	l_y.append(y)

# 전체 좌표에서 판다가 있는지 판단
# 없는 좌표이면, 거리를 합산 (리스트로 저장?)
# 거리가 가장 낮은걸로 판단

def distance_find (a, b, x, y):
	return (a - x)**2 + (b-y)**2

#아주 큰값으로 설정
min_distance = float('inf')

# 전체좌표(p,q)에 대해서 판다좌표(l_x,l_y) 겹치는지 확인
for q in range(1, n+1):
	for p in range(1, m+1):
		
		# 판다랑 안겹치면
		if (p,q) not in [(l_x[i],l_y[i]) for i in range(k)]:
			result = 0  #초기화
			
			# 결과값 누적하기
			for r in range(k):
				result += distance_find(p, q, l_x[r],l_y[r])

			# 최솟값 갱신하기
			min_distance = min(min_distance, result)
			
print(min_distance)