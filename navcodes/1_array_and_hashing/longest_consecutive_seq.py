from typing import List
from collections import defaultdict

class LongestConsecutive:
    # Brute Force (O(N^2))
    def brute_force(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1 
            res = max(res, streak)
        return res
    
    # Hash Set Optimized (O(N))
    def using_hash_set(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:  # start of a sequence
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    
    # Hash Map (Union-Find Style) (O(N))
    def using_hash_maps(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res


if __name__ == "__main__":
    solver = LongestConsecutive()
    nums = [100, 4, 200, 1, 3, 2]

    print("Input:", nums)
    print("Brute Force:", solver.brute_force(nums))
    print("Using Hash Set:", solver.using_hash_set(nums))
    print("Using Hash Maps:", solver.using_hash_maps(nums))
