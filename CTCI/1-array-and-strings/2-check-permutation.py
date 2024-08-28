class CheckPermutation:
    '''
    Check Permutation: Given two strings, write a method to decide if one is a permutation of the other. 

    '''
    def using_sort(self, s1, s2):
        if len(s1) != len(s2):
            return False
        s1,s2 = sorted(s1), sorted(s2)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        return True
    
    def by_count(self, s1, s2):
        if len(s1) != len(s2):
            return False
        counter = [0] * 256
        for ch in s1:
            counter[ord(ch)] += 1
        for ch in s2:
            if counter[ord(ch)] == 0:
                return False
            counter[ord(ch)] -= 1
        return True
    
    def check_permutation_pythonic(self, s1, s2):
        from collections import Counter
        if len(s1) != len(s2):
            return False
        return Counter(s1) == Counter(s2)
