values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40, 
    "XC": 90,
    "CD": 400,
    "CM": 900
}

class Solution:
    def romanToInt(self, s):
        total = 0
        i = 0
        while i < len(s):
            # If i hasn't hit the end of the list, and is two characters in values (XC, CD, etc.)
            if i < len(s) - 1 and s[i:i+2] in values:
                print(s[i:i+2])
                total += values[s[i:i+2]] 
                # jump by two characters, because they've been added
                i += 2
            # Just add to total
            else:
                print(s[i])
                total += values[s[i]]
                i += 1
        return total
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # take x and reverse order using ::-1 to start at the end and copy in order
        if x == x[::-1]:
            return True
        else:
            return False

print(Solution().romanToInt("MCMXCIV"))
print(Solution().isPalindrome(121))
