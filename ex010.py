class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        
        if not s:
            return 0
        
        sign = 1
        i = 0
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            i += 1
        
        number = 0
        while i < len(s) and s[i].isdigit():
            number = number * 10 + int(s[i])
            i += 1
        
        number *= sign
        
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if number < INT_MIN:
            return INT_MIN
        if number > INT_MAX:
            return INT_MAX
        return number
