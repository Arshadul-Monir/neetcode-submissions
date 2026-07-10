class Solution:
    def candy(self, ratings: List[int]) -> int:
        c = len(ratings)
        candies = [1] * c
        count = 0

        for i in range(1, c):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        for i in range(c - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i + 1] + 1, candies[i])
            count += candies[i]
        
        return count + candies[c - 1]