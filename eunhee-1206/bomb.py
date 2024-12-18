import sys
input = sys.stdin.readline

# 입력 처리
N, K = map(int, input().split())
T_map = []
for i in range(N):
    s = list(map(int, input().split()))
    T_map.append(s)

# 8방향 이동 리스트 (상하좌우 + 대각선)
move_list = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

# 깃발 중 값이 K인 개수를 저장할 변수
flag_count = 0

# 게임판 순회
for i in range(N):
    for j in range(N):
        if T_map[i][j] == 0:  # 구름이 없는 칸이면
            cloud_count = 0  # 인접한 구름 칸의 개수
						# 8방향으로 인접한 칸을 확인
            for dx, dy in move_list:
                nx = i + dy  # 새로운 행
                ny = j + dx  # 새로운 열
                
                # 인접한 칸이 유효 범위 내에 있는지 확인
                if 0 <= nx < N and 0 <= ny < N:
                    if T_map[nx][ny] == 1:  # 구름이 있는 칸이면
                        cloud_count += 1
            
            # 인접한 구름의 개수가 K와 같으면 flag_count 증가
            if cloud_count == K:
                flag_count += 1

# 결과 출력
print(flag_count)
