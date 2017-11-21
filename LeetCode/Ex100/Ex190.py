class Ex190:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        a = bin(n)
        a = a[2:]
        #pre = 
        a = '0' * (32 - len(a)) + a
        a = a[::-1]
        #print a
        res = int(a, 2)
        return res
    '''
    def reverseBits(self, n):
        oribin='{0:032b}'.format(n)
        reversebin=oribin[::-1]
        return int(reversebin,2)
    '''
    '''
    public int reverseBits(int n) {
        int result = 0;
        for (int i = 0; i < 32; i++) {
            result += n & 1;
            n >>>= 1;   // CATCH: must do unsigned shift
            if (i < 31) // CATCH: for last digit, don't shift!
                result <<= 1;
        }
        return result;
    }
    '''
    ''' # !!!
    class Solution {
    public:
        uint32_t reverseBits(uint32_t n) {
            n = (n >> 16) | (n << 16);
            n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8);
            n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4);
            n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2);
            n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1);
            return n;
        }
    };
    for 8 bit binary number abcdefgh, the process is as follow:

    abcdefgh -> efghabcd -> ghefcdab -> hgfedcba
    '''
    
ex190 = Ex190()
n = 5
n = 43261596
print 190, ex190.reverseBits(n)

