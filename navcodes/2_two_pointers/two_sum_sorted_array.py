class TwoSum:
    def two_pointers(self, nums, target):
        """
        Two-pointer solution for the 'Two Sum II' problem.
        Assumes nums is sorted in non-decreasing order.
        Returns 1-indexed positions of the two numbers.
        """
        l, r = 0, len(nums) - 1

        while l < r:
            curr_sum = nums[l] + nums[r]
            if curr_sum > target:
                r -= 1
            elif curr_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]  # 1-indexed
        return []

if __name__ == "__main__":
    solver = TwoSum()

    # Test Case 1
    nums = [2, 7, 11, 15]
    target = 9
    print("Input:", nums, "Target:", target)
    print("Output:", solver.two_pointers(nums, target))  # [1, 2]

    # Test Case 2
    nums = [2, 3, 4]
    target = 6
    print("Input:", nums, "Target:", target)
    print("Output:", solver.two_pointers(nums, target))  # [1, 3]

    # Test Case 3
    nums = [-1, 0]
    target = -1
    print("Input:", nums, "Target:", target)
    print("Output:", solver.two_pointers(nums, target))_
