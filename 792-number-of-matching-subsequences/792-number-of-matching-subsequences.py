class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=[i]
            else:
                d[s[i]].append(i)
        print(d) 
        c=0
        for word in words:
            t=-1
            f=1
            for l in word:
                if l not in d:
                    f=0
                    break
                idx=bisect_right(d[l],t)
                if idx==len(d[l]):
                    f=0
                    break
                t=d[l][idx]   
                print(t)
            if f:
                c+=1
                    
                
                
                   
        return c       
                
        