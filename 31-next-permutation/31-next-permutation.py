class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n=len(nums)    
        # i=n-2
        # while(i>=0 and nums[i]>=nums[i+1]):
        #     i-=1  
        # if i==-1:
        #     nums=nums[::-1]
        # else:
        #     for k in range(n-1,i,-1):
        #         if(nums[i]<nums[k]):
        #             nums[i],nums[k]=nums[k],nums[i]
        #     nums[i+1:n]=nums[n-1:i:-1]  
        # print(nums)   
        n = len(nums)
        index_1, index_2 = 0, 0
        for i in range(n-2, 0, -1):
            if nums[i] < nums[i+1]:
                index_1 = i
                break

        for i in range(n-1, 0, -1):
            if nums[i] > nums[index_1]:
                index_2 = i
                break
        
        nums[index_1], nums[index_2] = nums[index_2], nums[index_1]
        if index_1 == 0 and index_2 == 0:
            nums[:] = nums[::-1]
        else:
            nums[index_1+1: ] = nums[:index_1:-1]
        
        