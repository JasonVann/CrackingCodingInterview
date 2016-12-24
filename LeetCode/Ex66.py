
class Ex66(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = 1
        l = len(digits)
        carry = 1
        while carry == 1:
            if i == l and digits[l - i] == 9:
                digits[l - i ] = 0
                digits.insert(0, 1)
                carry = 0
            elif (digits[l - i] == 9):
                digits[l - i] = 0
                i += 1
            else:
                digits[l - i] += 1
                carry = 0
        return digits
            
ex66 = Ex66()
test1 = [9, 9, 9, 9]
test2 = [1]
print 66, ex66.plusOne(test1)
