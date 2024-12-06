n = int(input())
h = list(map(int, input().split()))

#총알 1사이클 뎀지가 10, 10을 기본단위로 생각
#리스트를 몫과 나머지로 분리
h_main = list(map(lambda x: x//10, h)) #메인타격 횟수
h_sub = list(map(lambda x: x%10, h))   #잔여체력

kill = 0         #처치 횟수
i = 0    # 잔여타격 횟수
j = 0   

while kill < n:
	if h_sub[j] > 0:    #체력이 0보다 크면, 체력을 깎는다
		h_sub[j] -= (1 + i%4)   # 1, 2, 3, 4를 반복해서 뺀다.
		i += 1
	else:
		j += 1
		kill += 1	  # 체력이 0이하이면, 처치

# j는 kill과 같은값을 가짐

result = sum(h_main) * 4 + i
print (result)
