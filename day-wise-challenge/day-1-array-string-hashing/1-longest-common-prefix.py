'''
LONGEST COMMON PREFIX

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''

class LogestCommonPrefix:
    def solution(self, words):
        if len(strs) == 1:
            return strs[0]
        strs = sorted(strs)
        for i in range(min(len(strs[0], len(strs[-1])))):
            if strs[0][1] != strs[-1][i]:
                return strs[0][:i]
        return strs[0]
        