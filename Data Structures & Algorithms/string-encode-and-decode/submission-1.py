class Solution:

    def encode(self, strs: List[str]) -> str:
        #store encoded msg
        res = ''
        #encode using int and pound prefix to mark length of word
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        #loop through array
        while i < len(s):
            j = i

            #get length of encoded word
            while s[j] != '#':
                j += 1

            #slice word out of encoded msg and add to list
            length = int(s[i:j])
            res.append(s[j+1: j + 1 + length])
            i = j + 1 + length

        return res