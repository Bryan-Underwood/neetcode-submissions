from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

            hashmap = {}

            #loop through each word
            for word in strs:
                
                #create a sorted key for each word
                key = ''.join(sorted(word))

                #check if key has been saved already
                if key in hashmap:
                    #if it has append the new word to the group
                    hashmap[key].append(word)

                else:
                    #add key and word to hashmap
                    hashmap[key] = [word]

            #create a list of arrays out of the hashmap
            res = list(hashmap.values())
            return res