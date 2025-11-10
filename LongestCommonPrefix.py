class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre=""
        if len(strs)==1:
            return strs[0]
        fl=False
        m=min(len(i) for i in strs)
        for i in range(m):
            for j in range(len(strs)-1):
                if strs[j][i]==strs[j+1][i]:
                    fl=True
                else:
                    return pre
            if fl:
                pre+=strs[0][i]
        
        return pre
        

            
