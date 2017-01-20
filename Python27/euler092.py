import PE_Lib
import sys
def unionFind(num, uf):
	stack = [num]
	while uf[stack[-1]] != 1 and uf[stack[-1]] != 81:
		stack.append(PE_Lib.sumOfDigits(stack[-1], 2))

	while len(stack) > 1:
		last = stack.pop()
		uf[stack[-1]] = uf[last]


def countCycles( limit ):
	#uf = {}
	#for i in range(1, limit+1):
	#	uf[i] = i
	uf = [i for i in xrange(1, limit+1)]
	for i in xrange(1, limit+1):
		unionFind(i, uf)

	count = 0
	for i in xrange(1, limit+1):
		if uf[i] == 81:
			count += 1
	return count

def main():
	#sys.setrecursionlimit(2000)
	print countCycles(10000000)
    
    
if __name__ == "__main__":
    main()