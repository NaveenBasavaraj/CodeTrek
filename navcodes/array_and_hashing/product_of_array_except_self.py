class Solution:
    def prod_of_array_except_self(self, nums):
        res = [1] * len(nums)

        # Prefix pass
        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # Postfix pass
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4]
    output = sol.prod_of_array_except_self(nums)
    print("Input:", nums)
    print("Output:", output)
