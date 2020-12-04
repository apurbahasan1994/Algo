class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        lokkup={keys:items for items,keys in enumerate(order)}
        def lex_order(w1,w2):
            for c1,c2 in zip(w1,w2):
                if lokkup[c1] < lokkup[c2]: return True
                if lokkup[c1] > lokkup[c2]: return False
            return len(w1) <= len(w2)
        for w1,w2 in zip(words,words[1:]):
            if lex_order(w1,w2):return True
        return False

sol=Solution()
print(sol.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"))