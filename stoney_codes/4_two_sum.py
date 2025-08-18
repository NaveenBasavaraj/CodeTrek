# problem: Given list of nums and target, find index of two nums that add up to target. Guaranteed to have the two unique nums.

# solution O(N): loop through nums, sub each num from target, search for difference in already seen dict
# if difference found, return indexes

class TwoSum:
    def retIndexes(self, nums, target):
        seen = {} # dictionary

        for i, val in enumerate(nums):
            k = abs(target - val)
            if k not in seen:
                seen[val] = i
            else:
                return (seen[k], i)


if __name__ == '__main__':
    x = TwoSum()
    print(x.retIndexes([2,11,7,15],9))