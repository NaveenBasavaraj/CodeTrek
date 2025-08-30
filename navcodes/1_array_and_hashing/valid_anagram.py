class Solution:
    def is_valid_anagram(self, s1, s2):
        # using hashing with dict
        if len(s1) != len(s2):
            return False
        counts1, counts2 = {}, {}
        for i in range(len(s1)):
            counts1[s1[i]] = 1 + counts1.get(s1[i], 0)
            counts2[s2[i]] = 1 + counts2.get(s2[i], 0)
        return counts1 == counts2  # FIX: compare dicts, not strings
    
    def is_valid_anagram_array(self, s1, s2):
        # using array hashing (optimized for lowercase English letters)
        if len(s1) != len(s2):
            return False
        
        count = [0] * 26
        for i in range(len(s1)):
            count[ord(s1[i]) - ord('a')] += 1
            count[ord(s2[i]) - ord('a')] -= 1
        for val in count:
            if val != 0:
                return False
        return True
    
    def isAnagram(self, s: str, t: str) -> bool:
        # using sorting
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


if __name__ == "__main__":
    sol = Solution()

    # test cases
    print(sol.is_valid_anagram("listen", "silent"))  # True
    print(sol.is_valid_anagram("rat", "car"))        # False

    print(sol.is_valid_anagram_array("listen", "silent"))  # True
    print(sol.is_valid_anagram_array("rat", "car"))        # False

    print(sol.isAnagram("listen", "silent"))  # True
    print(sol.isAnagram("rat", "car"))        # False
