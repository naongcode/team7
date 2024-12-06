a = int(input())

b = []
for i in range(a):
	b.append(i+1)

for k in range(1,a+1):
	c = list(map(lambda x: x*k, b))
	print(*c)