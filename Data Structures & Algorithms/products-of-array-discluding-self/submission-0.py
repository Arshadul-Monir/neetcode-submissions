class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        product = 1

        for idx, i in enumerate(nums):
            output[idx] = product
            product *= i
        
        product = 1
        for idx, i in enumerate(nums[::-1]):
            output[len(nums) - 1 - idx] *= product
            product *= i
        
        return output

