import navlogs
# Problem: Check for duplicates

class ContainsDuplicates:
    @navlogs.debug
    def optmized_solution(self, nums):
        # O(N)
        # using set()
        if not nums:
            return False
        
        return len(nums) == len(set(nums))


if __name__ == '__main__':
    sol = ContainsDuplicates()
    print(sol.optmized_solution([1,2,3,1]))
    print(sol.optmized_solution([1,2,3,4]))