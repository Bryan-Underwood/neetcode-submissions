class Solution:
    def isValid(self, s: str) -> bool:
        #map each bracket
        hashmap = { ')' : '(', ']' : '[', '}' : '{', }
        stack = []

        #loop through array
        for b in s:
            #if bracket is not a closing bracket add to stack
            if b not in hashmap:
                stack.append(b)

            else:
                #if stack is empty there is a left over closing bracket
                #if the top of the stack does not match the equivalant opening bracket
                if not stack or stack.pop() != hashmap[b]:
                    return False

        return not stack