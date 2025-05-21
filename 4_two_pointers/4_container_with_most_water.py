class BiggestContainer:
    def maxArea(self, wall_heights):
        res = 0
        l = 0
        r = len(wall_heights) - 1
        while l < r :
            area = (r-l) * min(wall_heights[l], wall_heights[r])
            res = max(res, area)

            if wall_heights[l] < wall_heights[r]:
                l += 1 
            else:
                r -= 1
        return res

if __name__ == '__main__':
    bc = BiggestContainer()
    print(bc.maxArea([1,8,6,2,5,4,8,3,7]))
