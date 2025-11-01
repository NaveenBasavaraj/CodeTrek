def binary_search(sorted_nums, l, r, val):
    if l > r:
        return -1
    
    mid = (l + r) // 2
    
    if sorted_nums[mid] > val:
        return binary_search(sorted_nums, l, mid - 1, val)
    elif sorted_nums[mid] < val:
        return binary_search(sorted_nums, mid + 1, r, val)
    else:
        return mid

# Test it
if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11]
    print(binary_search(nums, 0, len(nums) - 1, 7))  # Output: 3
    print(binary_search(nums, 0, len(nums) - 1, 4))  # Output: -1
