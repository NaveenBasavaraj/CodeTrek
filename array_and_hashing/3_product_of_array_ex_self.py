class ProductArray:
    def prePostFix(self, nums):
        if len(nums) <= 1:
            return nums
        
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = postfix
            postfix *= nums[i]
        return res 

if __name__ == "__main__":
    pa = ProductArray()
    print(pa.prePostFix([1,2,3,4]))