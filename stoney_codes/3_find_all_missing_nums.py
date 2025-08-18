# problem: Given list [1,N], find all the missing nums between 1 to N and add it to a new list.
# return new list

# Solution O(N) time and space: loop from 1, N is num not in set(nums) add it to new list.

class MissingNumber:
    def retList(self, nums):
        ret = []
        nums = set(nums)

        for i in range(1, len(nums)+1):
            if i not in nums:
                ret.append(i)
        return ret 

if __name__ == '__main__':
    x = MissingNumber()
    print(x.retList([1,2,3,5]))