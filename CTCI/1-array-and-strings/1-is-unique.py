class IsUnique:
    '''
    Is Unique: Implement an algorithm to determine if a string has all unique characters. 
    What if you cannot use additional data structures?
    '''
    def using_set(self, string):
        '''
         using set function
         either using length of set matches 
         or checking if char is already seen
        '''
        # return len(set(string)) == len(string)
        seen = set()
        for ch in strings:
            if ch in seen:
                return False
            seen.add(ch)
        return True
    
    def is_unique_chars_hash_index(self, string):
        if len(string) > 128:
            # i.e not ascii
            return False
        
        char_map = [False] * 128
        for char in string:
            ascii_val = ord(char)
            if char_map[val]:
                return False
            char_map[ascii_val] = True
        return True
    
    def using_bit_vector(self, string):
        if len(string) > 128:
            return False
        checker = 0
        for ch in string:
            val = ord(ch)
            if (checker & (1 << val)) > 0:
                return False
            checker = checker | (1 << val)
        return True



if __name__ == "__main__":
    print()
