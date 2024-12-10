import sys
input = sys.stdin.readline

N = int(input())
M = []

for i in range(1, N+1):
	row = []
	for j in range(1,N+1):
		row.append(i*j)
	M.append(row)
	
for row in M:
    print(' '.join(map(str, row)))
