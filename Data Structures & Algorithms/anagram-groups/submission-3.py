class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublist=defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            sublist[sortedS].append(s)
        return list(sublist.values())