class Solution:
    def triangleType(self, nums:list[int]) -> str:
            if nums[0] + nums[1] > nums[2] and nums[1] + nums[2] > nums[0] and nums[0] + nums[2] > nums[1]:
                if nums[0] == nums[1] == nums[2]:
                    return "equilateral"
                elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2] :
                    return "isosceles"
                else:
                    return "scalene"
            else:
                return "none"
triangolo1:Solution = Solution()
print(triangolo1.triangleType([3,3,3]))