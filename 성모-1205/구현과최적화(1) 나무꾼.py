#입력받기
n, m, x = map(int, input().split()) # 나무수, 벌목높이, 시작위치
a = list(map(int, input().split())) # 초기높이
q = int(input())                    # 벌목횟수
d = list(input().split())           # 움직이는방법

# 메인논리
# 높이가 +1되는 것을 따로 저장함.
# 벌목판단할때는 높이증가량과, 벌목으로인한 감소량을 동시에 고려
# -> 나무의 현재높이 = 초기값 + 증가량 - 감소량
acc = 0 # 증가량
cut_list = [0]*n # 감소량을 저장할 리스트

x = x-1   #위치를 인데스랑 같게 조정

for i in range(q):
	if (a[x] + acc - cut_list[x]) >= m:  # 현재높이가 기준값이상이면
		cut_list[x] += a[x] + acc - cut_list[x]  # 리스트에 현재 값을 누적
		
	# 다음위치 판정
	if d[i] == "L":
		x = (x-1)%n
	elif d[i] == "R":
		x = (x+1)%n
	acc +=1 #증가
	
	# print("x:",x,"acc:",acc,"cut:",cut_list)  #중간내용볼려고 만들어놓음
	
print(sum(cut_list))
