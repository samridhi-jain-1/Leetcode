class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)    
        i=n-2
        while(i>=0 and nums[i]>=nums[i+1]):
            i-=1  
        print(i)    
        if i==-1:
            nums[::]=nums[::-1]
        else:
            for k in range(n-1,i,-1):
                if(nums[i]<nums[k]):
                    print(k)
                    nums[i],nums[k]=nums[k],nums[i]
                    break
            print(nums)        
            nums[i+1:n]=nums[n-1:i:-1]  
           


        
        