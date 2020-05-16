class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return []
        self.result = []
        self.minlength = math.inf
        self.find(beginWord, endWord, wordList, [])
        return self.result

    def check(self,w1, w2):
        ch = 0
        for i in range(len(w1)):
            if w1[i] == w2[i]:
                ch += 1
        return abs(ch - len(w1)) == 1

    def find(self,begin, end, lst, temp):
        temp.append(begin)
        if begin == end:
            if len(temp) == self.minlength:
                self.result.append(temp.copy())
            elif len(temp) < self.minlength:
                self.result = [temp.copy()]
                self.minlength = len(temp)
        else:
            if lst:
                for w in lst:
                    if self.check(w, begin):
                        index = lst.index(w)
                        del lst[index]
                        self.find(w, end, lst.copy(), temp)
                        temp.pop()
