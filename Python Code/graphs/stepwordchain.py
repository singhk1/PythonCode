from collections import deque
from string import ascii_lowercase

def word_ladder(start, end, words):
    queue = deque([(start,[start])])

    while queue:
        word, path = queue.popleft()
        if word == end:
            return path

        for i in range(len(word)):
            for char in ascii_lowercase:
                next_word = word[:i] + char + word[i + 1:]
                if next_word in words:
                    words.remove(next_word)
                    queue.append([next_word, path + [next_word]])
    return None

start = "dog"
end = "cat"
words = {"dot", "dop", "dat", "cat"}
words2 = {"dot", "tod", "dat", "dar"}
print(word_ladder(start, end, words))
print(word_ladder(start, end, words2))
