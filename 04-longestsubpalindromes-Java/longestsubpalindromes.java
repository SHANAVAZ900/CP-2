// # Write the function longestSubpalindrome(s), that takes a string s and returns 
// the longest palindrome that occurs as consecutive characters (not just letters, but 
// 	any characters) in s. So:
// #    	longestSubpalindrome("ab-4-be!!!") 
// # returns "b-4-b". If there is a tie, return the lexicographically larger value -- 
// in java, a string s1 is lexicographically greater than a string s2 if (s1 > s2). So:
// #    	longestSubpalindrome("abcbce") 
// # returns "cbc", since ("cbc" > "bcb"). Note that unlike the previous functions, 
// this function is case-sensitive (so "A" is not treated the same as "a" here). Also, 
// from the explanation above, we see that longestSubpalindrome("aba") is "aba", 
// and longestSubpalindrome("a") is "a".

class longestsubpalindromes {
	public String fun_longestsubpalindromes(String s) {
		int total = s.length(), count = 0;
		if (total == 1)
			return s;
		StringBuilder last = new StringBuilder();
		last.append(s);
		last = last.reverse();
		String palindromesub = "";
		for (int i = 0; i < total; i++) {
			for (int j = total - 1; j > i; j--) {
				String k = s.substring(i, j + 1), y = last.substring(total - j - 1, total - i);
				if (k.equals(y) && k.length() > palindromesub.length())
					palindromesub = k;
				else if (k.equals(y) && k.length() == palindromesub.length() && k.compareTo(palindromesub) > 0)
					palindromesub = k;
			}
		}
		return palindromesub;
	}

	public static void main(String[] args) {

	}
}