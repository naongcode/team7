import sys
input = sys.stdin.readline

N, K = map(int, input().split())  
origin_list = list(map(int, input().split()))  

# 각 숫자에 대해 이진수로 변환하고 1의 개수를 셈
DtoB = [(x, bin(x).count('1')) for x in origin_list]

# 이진수에서 1의 개수를 기준으로 내림차순 정렬하고, 1의 개수가 같으면 10진수 값을 기준으로 내림차순 정렬
DtoB.sort(key=lambda x: (x[1], x[0]), reverse=True)

# K번째 위치의 값 추출 
print(DtoB[K-1][0])
