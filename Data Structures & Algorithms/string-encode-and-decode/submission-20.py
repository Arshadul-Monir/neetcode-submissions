class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for word in strs:
            output += str(len(word)) + "#" + word
        
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        idx = 0
        counter = 0
        while idx < len(s):
            # print(s, idx)
            if counter == 0:
                counter_str = ""
                while s[idx] != "#":
                    counter_str += s[idx]
                    idx += 1
                counter = int(counter_str)
                idx += 1

            curr = ""
            while counter > 0:
                curr += s[idx]
                idx += 1
                counter -= 1
            output.append(curr)

        return output



            