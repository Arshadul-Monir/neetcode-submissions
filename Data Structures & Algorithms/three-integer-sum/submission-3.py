class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        print()
        works = []
        for i in range(len(nums) - 2):
            if i != 0 and nums[i-1] == nums[i]:
                continue
            first = nums[i]
            left = i + 1
            right = len(nums)-1
            while left < right:
                if first + nums[left] + nums[right] < 0:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        print("test1")
                        left += 1

                elif first + nums[left] + nums[right] > 0:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        print("test2")
                        right -= 1
                else:
                    print(i, left, right)
                    works.append([first, nums[left], nums[right]])
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        print("test2")
                        right -= 1

        return works
        