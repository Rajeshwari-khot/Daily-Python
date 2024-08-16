
--kids with greatest number of candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr=[]
        maxcandies=max(candies)
        for i in range (len(candies)):
            if candies[i]+extraCandies>=maxcandies:
                arr.append(True)
            else:
                arr.append(False)
        return arr
