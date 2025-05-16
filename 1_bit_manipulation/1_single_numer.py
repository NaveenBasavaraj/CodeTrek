class SingleNumber:
    '''
    You are given a non-empty array of integers nums. Every integer appears twice except for one.
    Return the integer that appears only once.
    O(n)
    '''
    def find(self, nums):
        res = 0
        for num in nums:
            res = num ^ res
        return res 

if __name__ == "__main__":
    sn = SingleNumber()
    print(sn.find([2,3,2,4,5,4,5]))