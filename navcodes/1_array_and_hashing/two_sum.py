class Solution:
    def two_sum(self, nums, target):
        diff_dict = {}

        for i, num in  enumerate(nums):
            diff = target - num
            if diff in diff_dict:
                return (i, diff_dict[diff])
            else:
                diff_dict[diff] = i

if __name__ == "__main__":
    s = Solution()
    print(s.two_sum([2, 7, 11, 15], 9))   # → (1, 0)
    print(s.two_sum([3, 2, 4], 6))        # → (2, 1)
    print(s.two_sum([3, 3], 6))           # → (1, 0)