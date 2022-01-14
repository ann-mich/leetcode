'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        bracketmap = {}
        bracketmap[')'] = '('
        bracketmap[']'] = '['
        bracketmap['}'] = '{'
        
        openbrackets = set()
        openbrackets.add('(')
        openbrackets.add('[')
        openbrackets.add('{')
        
        stack = []
        for c in s:
            if c in openbrackets:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    prev = stack[-1]
                    if bracketmap[c] == prev:
                        stack.pop()
                    else:
                        return False
        return stack == []
        
        
# Time complexity: O(N)
# Space complaexity: O(N)
