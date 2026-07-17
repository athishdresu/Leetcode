class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pair={
            '(':')',
            '{':'}',
            '[':']'
        }
        for ch in s:
            if ch in pair:
                stack.append(pair[ch])
            else:
                if not stack or stack.pop()!=ch:
                    return False
        return not stack