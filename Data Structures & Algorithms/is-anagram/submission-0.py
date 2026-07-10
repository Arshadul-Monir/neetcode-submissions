class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}

        for i in s:
            s_dict[i] = s_dict.get(i, 0) + 1

        for i in t:
            if i in s_dict:
                s_dict[i] -= 1
                if not s_dict[i]:
                    s_dict.pop(i)
            else:
                return False
        
        return not s_dict

        