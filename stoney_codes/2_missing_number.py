# problem : missing number between 0 to N, given N.

# Solution 1 O(N) : Iterate through list and get expected sum and actual sum

# solution 2 O(N) : Iterate through list and get actual sum. Use n(n+1)/2 formula to get expected sum
import navlogs

class MissingNumber:
    @navlogs.debug
    def findNum(self, nums):
        return sum(range(len(nums)+1)) - sum(nums)
    @navlogs.debug
    def findNumOpt(self, nums, n):
        return (n*(n+1))//2 - sum(nums)
    @navlogs.debug
    def findNumSort(self, nums):
        nums.sort()
        for i, v in enumerate(nums):
            if i != v:
                return i
        return 0
    

if __name__ == '__main__':
    x = MissingNumber()
    print(x.findNum([0,3,1], 3))
    print(x.findNumOpt([0,3,1], 3))
    print(x.findNumSort([0,3,1], 3))