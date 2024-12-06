#입력받기
n = int(input())
a = []
for i in range(n):
	b = int(input())
	a.append(b)

# 조건을 만족하려면 A는 소수 이어야 함
def is_prime(c):
	if c <= 3:  #2와 3은 소수
		return "Yes"
	if c%2 ==0 or c%3==0:  #2, 3으로 나누어떨어지면 소수아님
		return "No"
	
	# 6k+-1만 소수가 될 수 있음
	i = 5
	while i**2 <= c:
		#5와 7을 비교, 이후 주기를6으로 계속비교
		if c%i ==0 or c%(i+2) ==0:
			return "No"
		i += 6
	return "Yes"

for j in a:
	print(is_prime(j))