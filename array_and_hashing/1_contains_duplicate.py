class CheckDuplicate:
    def usingSet(self, nums):
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False
    
    def usingSetLen(self, nums):
        return len(set(nums)) != len(nums)
    
    def usingSortAndIndexing(self, nums):
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        
        return False 


if __name__ == "__main__":
    cd = CheckDuplicate()
    nums = [1,7,8,9,10]
    print(f'nums: {nums}')
    print(cd.usingSet(nums))
    print(cd.usingSetLen(nums))
    print(cd.usingSortAndIndexing(nums))
    nums = [1,7,8,9,1]
    print(f'nums: {nums}')
    print(cd.usingSet(nums))
    print(cd.usingSetLen(nums))
    print(cd.usingSortAndIndexing(nums))

