n = int(input())
a = []
for i in range(n):
	b = int(input())
	a.append(b)

# 소수 판정
def is_prime(x):
	if x <= 3:
		return True
	elif x%2 ==0 or x%3 ==0:
		return False
	i =5
	while i**2 <= x:
		if x%i==0 or x%(i+2)==0:
			return False
		i +=6
	return True

for j in range(n):
	result = 0
	#소수가 아니면 -1, 소수일때까지 반복
	while not is_prime(a[j]):
		a[j] = a[j] -1
		result +=1	

	print(result)