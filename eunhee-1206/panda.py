import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())

pandas = []
for i in range(K):
    R, C = map(int,input().split())
    pandas.append((R, C))


min_not_contentment = float('inf')
goorm_location = 0

#전체 격자 탐색
for r in range(1, N+1): 
    for c in range(1, M+1):
        if (r, c) not in pandas: #판다랑 안 마주쳤다면
            not_contentment = 0 #현재 칸을 0으로

            #전체 판다와의 거리 계산
            for panda_r, panda_c in pandas: 
                not_contentment += (r - panda_r) ** 2 + (c - panda_c) ** 2

            #현재 칸의 불만족도가 최소값이라면 그것으로 대체
            min_not_contentment = min(min_not_contentment, not_contentment)

#불만족도가 가장 낮은 칸
print(min_not_contentment)