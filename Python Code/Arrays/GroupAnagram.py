from collections import defaultdict
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    ana = defaultdict(list)
    for word in strs:
        ana[''.join(sorted(word))].append(word)
    return [value for value in ana.values()]
