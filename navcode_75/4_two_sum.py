# problem: Given list of nums and target, find index of two nums that add up to target. Guaranteed to have the two unique nums.

# solution O(N): loop through nums, sub each num from target, search for difference in already seen dict
# if difference found, return indexes

class TwoSum:
    def retIndexes(self, nums, target):
        seen = {} # dictionary

        for i, val in enumerate(nums):
            k = target - val
            if val not in seen:
                seen[val] = i
            else:
                return (seen[val], i)