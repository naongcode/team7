n = int(input())

# 원본리스트
data_list = []
for i in range(n):
	a, b = list(map(int, input().split()))
	data_list.append([a,b])
	
# x, y순으로 정렬된 리스트
sorted_list = sorted(data_list, key = lambda x: (x[0],x[1]), reverse=True)

#
index_map = {tuple(value): index for index, value in enumerate(sorted_list)}

# 원본이 정렬된 리스트에서 어디에 위치해 있는지
for j in data_list:
	print(index_map[tuple(j)])

	
# for문안에서 배열.index를 썼더니 n제곱의 시간복잡도 발생
# 인덱스를 미리 계산해 놓는 방식을 사용해야함