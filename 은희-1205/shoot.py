import sys
input = sys.stdin.readline

N = int(input())  # 적의 수
H = list(map(int, input().split()))  # 각 적의 체력

shoot = 0  # 권총 발사 횟수
i = 0 #쓰러트린 적의 수

while i < N:
	if H[i] > 0: #적이 살아있음
		H[i] -= ((shoot) % 4) + 1 #데미지 주기
		shoot += 1  # 발사 횟수 증가
	else : #현재 적이 쓰러졌다면
		i += 1 #다음적으로 넘어가기


print(shoot)  # 총 발사 횟수 출력
