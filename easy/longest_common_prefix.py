from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(strs, key=len)
        prefix = ""
        for i in range(len(min_len)):
            charset = set([s[i] for s in strs])
            if len(charset) == 1:
                prefix = prefix + strs[0][i]
            else:
                break
            
        return prefix