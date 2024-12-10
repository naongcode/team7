import sys
import math
input = sys.stdin.readline

N = int(input()) #갑옷의 갯수
A = [int(input()) for _ in range(N)] #갑옷의 고윳값  

def is_prime_number(x): #소수 판별
	if x < 2:
		return "No"
	if x == 1:
		return "No"
	for i in range(2, int(math.sqrt(x))+1): #에라토스테네스의 체
		if x % i == 0:
			return "No"
	return "Yes"
	
	
for i in A:
	print(is_prime_number(i))
	

