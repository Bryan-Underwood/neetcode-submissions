from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #create a default dict to group words
        anagrams = defaultdict(list)

        for word in strs:

            #map each char in a word to its place in the alphabet
            count = [0] * 26
            for char in word:
                #increments a letter in the alphabet by one
                count[ord(char) - ord('a')] += 1

            #use the created list to create an imutable tuple as a key
            key = tuple(count)
            anagrams[key].append(word)

        return list(anagrams.values())