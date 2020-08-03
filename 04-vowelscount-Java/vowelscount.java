// # Write the function vowelCount(s), that takes a string s, 
// # and returns the number of vowels in s, ignoring case, 
// # so "A" and "a" are both vowels. The vowels are "a", "e", "i", "o", and "u". 
// # So, for example, ("Abc def!!! a? yzyzyz!") returns 3 (two a's and one e).

class vowelscount {
	public int fun_vowelscount(String s) {
		// your code goes here
		String low_str = s.toLowerCase();
		int count = 0;
		for (int i = 0; i <= low_str.length() - 1; i++) {
			if (low_str.charAt(i) == 'a' || low_str.charAt(i) == 'e' || low_str.charAt(i) == 'i'
					|| low_str.charAt(i) == 'o' || low_str.charAt(i) == 'u') {
				count++;
			}
		}

		return count;

	}

	public static void main(String[] args) {

	}

}