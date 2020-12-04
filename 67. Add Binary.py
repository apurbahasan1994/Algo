from collections import deque


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        result = deque()
        s = ''
        for i in range(max(len(a), len(b)) - min(len(a), len(b))):
            s += '0'
        if len(a) < len(b):
            a = s + a
        if len(b) < len(a):
            b = s + b

        for x, y in zip(reversed(a), reversed(b)):
            carry, reminder = divmod(int(x) + int(y) + carry, 2)
            result.appendleft(reminder)
        if carry:
            result.appendleft(carry)
        return ''.join(map(str, result))