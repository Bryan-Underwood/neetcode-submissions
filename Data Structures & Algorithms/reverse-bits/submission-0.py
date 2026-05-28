class Solution:
    def reverseBits(self, n: int) -> int:
        #store reversed bits into result
        res = 0
        #loop once per bit
        for _ in range(32):

            #get the last bit of number
            last = n & 1

            #shift result left to make room
            res <<= 1
            #place collected bit into result
            res |= last

            #move on to next bit in the number
            n >>= 1

        return res