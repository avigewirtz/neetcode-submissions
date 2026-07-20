class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        for s in strs:
            if ''.join(sorted(s)) in anagrams:
                anagrams[''.join(sorted(s))].append(s)
            else: 
                anagrams[''.join(sorted(s))] = [s]
        
        output = []

        for l in anagrams.values():
            output.append(l)
        
        return output


        