
class Solution:
    def minSum(self, arr, n):
        # Your code goes here
        if n<=2:
            return sum(arr)
        else:
            arr.sort()
            f=arr[0]
            s=arr[1]
            i=2
            while(i<n):
                f=f*10+arr[i]
                if(i+1<n):
                    s=s*10+arr[i+1]
                i+=2    
            return f+s     
    

#{ 
#  Driver Code Starts

import heapq as hq

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob=Solution()
        print(ob.minSum(arr,n))

# } Driver Code Ends