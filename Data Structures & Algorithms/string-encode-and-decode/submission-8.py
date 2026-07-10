class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        if ','.join(strs) == "":
            return "emPty"
        return 'EIEIOWOWOW'.join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        if s == "emPty":
            return [""]
        return s.split('EIEIOWOWOW')
