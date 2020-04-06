"""
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#     # Approach 1 : Using sorted string    
#     # Edge case
#     if len(strs) == 0:
#         return []
#     hash_map = {}
#     for s in strs:
#         sorted_str = ''.join(sorted(s))
#         # If not in hash_map
#         if sorted_str not in hash_map:
#             hash_map[sorted_str] = [s]
#         else:
#             hash_map[sorted_str].append(s)
#     return hash_map.values()
    
    # Approach 2 : Storing count of the alphabet of the word. 
    # Edge case
    if len(strs) == 0:
        return []
    # Storing the count
    hash_map = collections.defaultdict(list)
    for s in strs:
        count = [0]*26
        for c in s:
            count[ord(c)- ord('a')] += 1
        hash_map[tuple(count)].append(s)
    return hash_map.values()
