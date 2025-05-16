class TwoSum:
    def usingDict(self, nums, k):
        seen = dict()

        for i, val in enumerate(nums):
            target = k - val
            if target in seen:
                return (seen[target], i)
            else:
                seen[val] = i 
        return None

if __name__ == "__main__":
    ts = TwoSum()
    print(ts.usingDict([5,2,3,1], 8))
