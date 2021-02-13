# 리트코드 49
strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
    #anagrams = collections.defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()

print(groupAnagrams(strs))
