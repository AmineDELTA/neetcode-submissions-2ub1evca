class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], ""
        for i in strs:
            sizes.append(len(i))
        for n in sizes:
            res += str(n)
            res += ","
        res += '#'
        for h in strs:
            res += h
        return res


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        for sz in sizes:
            res.append(s[i:i +sz])
            i += sz
        return res
        
        return 