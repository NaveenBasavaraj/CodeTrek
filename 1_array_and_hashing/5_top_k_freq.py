class FreqElements:
    def topKfreq(self, nums):
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num in count:
            i = count[num]
            freq[i].append(num)
        
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res