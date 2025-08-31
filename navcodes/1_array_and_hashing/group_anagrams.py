from collections import defaultdict

class Solution:
    def group_anagrams(self, words):
        res = defaultdict(list) 
        for word in words:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1   # FIX: increment instead of assign
            res[tuple(count)].append(word)
        return list(res.values())


if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    output = sol.group_anagrams(words)
    print("Input:", words)
    print("Grouped Anagrams:", output)
