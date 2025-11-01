class Solution:
    def contains_duplicate(self, nums):
        if not nums:
            return False
        
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True 
        return False 
    
    def contains_duplicate_set(self, nums):
        return len(set(nums)) < len(nums)


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(Solution().contains_duplicate(nums))        # Output: False
    print(Solution().contains_duplicate_set(nums))    # Output: False

    nums = [1, 2, 3, 2]
    print(Solution().contains_duplicate(nums))        # Output: True
    print(Solution().contains_duplicate_set(nums))    # Output: True

    nums = []
    print(Solution().contains_duplicate(nums))        # Output: False
    print(Solution().contains_duplicate_set(nums))    # Output: False
    


