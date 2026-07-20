class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        for s in strs:
            if str(sorted(s)) in anagrams:
                anagrams[str(sorted(s))].append(s)
            else: 
                anagrams[str(sorted(s))] = [s]
        
        output = []

        for l in anagrams.values():
            output.append(l)
        
        return output


        