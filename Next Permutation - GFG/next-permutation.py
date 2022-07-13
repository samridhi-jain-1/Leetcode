#User function Template for python3

class Solution:
    def nextPermutation(self, n, arr):
        # code here
        i=n-2
        while(i>=0 and arr[i]>=arr[i+1]):
            i-=1
        if i==-1:
            arr[::]=arr[::-1]
        else:
            for k in range(n-1,i,-1):
                if(arr[i]<arr[k]):
                    arr[i],arr[k]=arr[k],arr[i]
                    break
            arr[i+1:]=arr[:i:-1]
        return arr    
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends