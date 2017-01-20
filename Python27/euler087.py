import PE_Lib
import math
from sets import Set

def primeQuadPower( limit ):
	primes = PE_Lib.sieve(limit + 1)
	used = set()

	for p1 in primes:
		psum1 = p1**4
		if psum1 > limit:
			break
		for p2 in primes:
			psum2 = psum1 + p2**3
			if psum2 > limit:
				break
			for p3 in primes:
				psum3 = psum2 + p3**2
				if psum3 >= limit:
					break
				used.add(psum3)

	return len(used)

def main():
    print primeQuadPower(50000000)
    
    
if __name__ == "__main__":
    main()