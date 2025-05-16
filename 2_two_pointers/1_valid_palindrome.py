class Palindrome:
    def isValid(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            while l<r and not self.isAlphaNum(s[l]):
                l += 1
            while l<r and not self.isAlphaNum(s[r]):
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
    
    def isAlphaNum(self, ch):
        return ((ord('a') <= ord(ch) <= ord('z')) or
               (ord('A') <= ord(ch) <= ord('Z')) or 
               (ord('0') <= ord(ch) <= ord('9')) )

if __name__ == "__main__":
    isp = Palindrome()
    print(isp.isValid("NAVEEN"))
    print(isp.isValid("NAVEEVAN"))