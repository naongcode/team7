import sys
input = sys.stdin.readline


N, M, x = map(int, input().split()) #나무수, 벌목높이, 시작위치
H = list(map(int, input().split())) #초기 높이
Q = int(input()) #벌목횟수
D = list(input().split()) #움직이는 방향


wood = 0 #벌목한 나무의 수

for i in range(Q): #벌목횟수 동안 
	if H[x-1] >= M: #만약 벌목 높이보다 벌목할 나무가 높다면
		wood += H[x-1] #벌목한 나무의 수에 넣은 뒤
		H[x-1] = 0 #벌목할 나무를 초기화한다.
		
	if D[i] == 'L':
		x = (x-1) % N
	elif D[i] == 'R':
		x = (x+1) % N
	
	H = [h + 1 for h in H] #모든 나무의 높이를 1씩 증가(다음 벌목을 하기 위함임)
		
print(wood)