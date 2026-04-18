class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = ''
        w2 = ''
        for ch in word1:
            w1+=ch
        for ch in word2:
            w2+=ch
        return w1 == w2