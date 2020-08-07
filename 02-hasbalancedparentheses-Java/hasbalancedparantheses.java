// # Write the function hasBalancedParentheses, which takes a string and returns True 
// # if that code has balanced parentheses and False otherwise (ignoring all 
// # 	non-parentheses in the string). We say that parentheses are balanced if each 
// # right parenthesis closes (matches) an open (unmatched) left parenthesis, 
// # and no left parentheses are left unclosed (unmatched) at the end of the text. 
// # So, for example, "( ( ( ) ( ) ) ( ) )" is balanced, but "( ) )" is not balanced, and "( ) ) (" 
// # is also not balanced. Hint: keep track of how many right parentheses remain unmatched as 
// # you iterate over the string.

import java.util.*;

class hasbalancedparantheses {
	public boolean fun_hasbalancedparantheses(String s) {
		if (s.length() == 0)
			return true;
		Stack<Character> last = new Stack<Character>();
		for (int i = 0; i < s.length(); i++) {
			char present = s.charAt(i);
			if (present == '{' || present == '[' || present == '(') {
				last.push(present);
			}
			if (present == '}' || present == ']' || present == ')') {
				if (last.isEmpty()) {
					return false;
				}
				char previous = last.peek();
				if (present == '}' && previous == '{' || present == ']' && previous == '['
						|| present == ')' && previous == '(') {
					last.pop();
				} else {
					return false;
				}
			}
		}
		return last.isEmpty() ? true : false;
	}

	public static void main(String[] args) {

	}
}
