class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        mx=nums[0]
        for i in range(len(nums)):
            
            sum+=nums[i]
            
            if sum>mx:
                mx=sum
            if(sum<0):
                sum=0
        return mx  
            
        