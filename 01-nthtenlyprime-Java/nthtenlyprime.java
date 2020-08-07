// # Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
// # and returns the nth Additive Prime, which is a prime number such that 
// # the s of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
// # is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

class nthtenlyprime {
	public int fun_nthtenlyprime(int n) {
		int c = 0;
		int v = 19;
		while (c < n) {
			v += 2;
			if (PrimeNum(v) && PrimeDigits(v) == 10)
				c += 1;
		}
		return v;
	}

	public int PrimeDigits(int num) {
		int s = 0;
		while (num > 0) {
			s += (num % 10);
			num /= 10;
		}
		return s;
	}

	public boolean PrimeNum(int num) {
		if (num <= 1)
			return false;
		else if (num == 2 || num == 3)
			return true;
		for (int i = 2; i <= (num / 2); i++) {
			if (num % i == 0)
				return false;
		}
		return true;
	}

	public static void main(String[] args) {
	}

}