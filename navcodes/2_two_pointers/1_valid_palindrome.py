class Solution:
    def isPalindromeTwoPointers(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[l]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
    
    def simpleIsPalindrome(self, s):
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    sol = Solution()
    print(sol.isPalindromeTwoPointers(s))   # True
    print(sol.simpleIsPalindrome(s))        # True

    s = "race a car"
    sol = Solution()
    print(sol.isPalindromeTwoPointers(s))   # False
    print(sol.simpleIsPalindrome(s))        # False

    s = "0P"
    sol = Solution()
    print(sol.isPalindromeTwoPointers(s))   # False
    print(sol.simpleIsPalindrome(s))        # False
