class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target == nums[i]+nums[j]:
                    return [i,j]

num=[1,2,3,4,5,6,7,8]  
target=3
s = Solution()
print(s.twoSum(num,target))
