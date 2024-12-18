import sys
input = sys.stdin.readline


N, M, x = map(int, input().split()) #나무수, 벌목높이, 시작위치
H = list(map(int, input().split())) #초기 높이
Q = int(input()) #벌목횟수
D = list(input().split()) #움직이는 방향


wood = 0 #벌목한 나무의 수

for i in range(Q):  # 벌목 횟수 동안
    # 현재 나무의 최종 높이를 계산
    current_height = H[x - 1] + total_increase

    if current_height >= M:  # 만약 벌목 높이보다 나무가 높다면
        wood += current_height  # 벌목한 나무의 수에 추가
        H[x - 1] = -total_increase  # 벌목한 나무는 누적 높이를 제거한 상태로 0으로 만듦

		
	if D[i] == 'L':
		x = (x-1) % N
	elif D[i] == 'R':
		x = (x+1) % N
	
	total_increase += 1 #모든 나무의 높이를 1씩 증가(다음 벌목을 하기 위함임)
		
print(wood)
