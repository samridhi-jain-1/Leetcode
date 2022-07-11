#User function Template for python3

def reaching_height (n, arr) : 
    #Complete the function
    arr.sort(reverse=True)
    i=0
    j=n-1
    ans=[]
    e=0
    o=0
    while(i<j):
        ans.append(arr[i])
        o+=arr[i]
        ans.append(arr[j])
        e+=arr[j]
        i+=1
        j-=1
    if(n&1):
        ans.append(arr[i])
        o+=arr[i]
    if e>=o:
        return [-1]
    return ans    
    
    
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = reaching_height(n, arr)
    if(len(ans) == 1 and ans[0] == -1):
        print("Not Possible")
    else:
        print(*ans)
# } Driver Code Ends