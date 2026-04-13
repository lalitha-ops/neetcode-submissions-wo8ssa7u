class Solution:
    def isValid(self, s: str) -> bool:
        d={')':'(','}':'{',']':'['}
        h=[]
        for char in s:
            if char in d.values():
                h.append(char)
            elif not h or h.pop()!=d[char]:
                return False
        return len(h)==0
            
