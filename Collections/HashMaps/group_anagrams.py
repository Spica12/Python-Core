# from collections import defaultdict

# class Solution:

#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagram_map = defaultdict(list)
#         result = []

#         for s in strs:
#             sorted_s = tuple(sorted(s))
#             anagram_map[sorted_s].append(s)

#         print(anagram_map)



# input_data = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

# Output = [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]