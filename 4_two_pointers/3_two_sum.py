class TwoSum:
    def twoPointer(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l < r:
            currSum = nums[l]+nums[r]
            if  currSum < target:
                l += 1
            elif currSum > target:
                r -= 1
            else:
                if currSum == target:
                    return (l+1,r+1)
        return ()
            
if __name__ == "__main__":
    ts = TwoSum()
    print(ts.twoPointer([1,3,4,5,7,10,11], 9))
