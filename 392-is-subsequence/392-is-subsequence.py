class Solution:
    def isSubsequence(self, A: str, B: str) -> bool:
        # sl=len(s)
        # tl=len(t)
        # if sl ==0:
        #     return True
        # if sl>tl:
        #     return False
        # i=0
        # k=0
        # while(i<sl and k<tl):
        #     if i==sl-1 and s[i]==t[k]:  
        #         return True
        #     if s[i]==t[k]:
        #         i+=1
        #     k+=1
        # return False     
        m=len(A)
        n=len(B)
        i=0
        j=0
        while(i<m and j<n):
            if(A[i]==B[j]):
                i+=1
            j+=1
        return i==m 