class ValidAnagram:
    def isAnagramCounting(self, s1,s2):
        if len(s1) != len(s2):
            return False
        map_s1 = {}
        map_s2 = {}

        for i in range(len(s1)):
            map_s1[s1[i]] = 1 + map_s1.get(s1[i], 0)
            map_s2[s2[i]] = 1 + map_s2.get(s2[i], 0)
        
        return map_s1 == map_s2
    
    def usingArrayCount(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        count = [0] * 26
        for i in range(len(s1)):
            count[ord(s1[i]) -ord('a')] += 1
            count[ord(s2[i]) -ord('a')] -= 1
        for val in count:
            if val != 0:
                return False
        return True
    
    def isAnagramSorting(self, s1, s2):
        if len(s1) != len(s2):
            return False
        return sorted(s1) == sorted(s2)

if __name__ == "__main__":
    isa = ValidAnagram()
    print(f'strings: rat tar')
    print(isa.isAnagramCounting('rat','tar'))
    print(isa.isAnagramSorting('rat','tar'))
    print(isa.usingArrayCount('rat','tar'))
    print(f'strings: car mar')
    print(isa.isAnagramCounting('car','mar'))
    print(isa.isAnagramSorting('car','mar'))
    print(isa.usingArrayCount('car','mar'))

    
        
