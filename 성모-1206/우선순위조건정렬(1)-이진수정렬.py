n, k = map(int, input().split())
a = list(map(int, input().split()))

# 2진수로 변환하면서, 동시에 1의 개수를 세기
c = [bin(x)[2:].count('1') for x in a] # [1,1,2,1,2,2,3,1]

# 배열 2개를 하나의 순서쌍으로 묶기
d = list(zip(a,c))  #[(1,1)(2,1)(3,2)(4,1)(5,2)(6,2)(7,3)(8,1)]

# 조건2개 적용하여 내림차순 정렬
result = sorted(d, key = lambda x:(x[1],x[0]), reverse=True)
### [(7,3)(6,2)(5,2)(3,2)(8,1)(4,1)(2,1)(1,1)]

# k 번째에서 앞자리 찾기
result_k = result[k-1][0]

#테스트용 출력
#print(a,"\n",c, "\n",d)
print(result_k)