class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        v=1
        ans=[]
        for j in range(rowIndex+1):
            ans.append(v)
            v=v*(rowIndex-j)//(j+1)
        return ans    
        
        