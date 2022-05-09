class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=nums[0]
        best=nums[0]
        for i in nums[1:]:
            curr+=i
            curr=max(curr,i)
            best=max(best,curr)
        return best    
#         sum=0
#         mx=nums[0]
#         for i in range(len(nums)):
            
#             sum+=nums[i]
#             if sum<0:
#                 sum=0
#             elif sum>mx:
#                 mx=sum
#         return mx  

            
        