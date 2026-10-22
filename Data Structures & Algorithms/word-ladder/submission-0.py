from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # given beginWord and endWord and a list conisting of words.
        # we want to transform beginWord into endWord.
        # we can transform beginWord to any word in wordList as long as only 1 char would be different in that word. 
        # we would then repeat this process with the new word we now have
        # return the min number of words it would take get to endWord.
        # return 0 if not possible

        if endWord not in wordList:
            return 0
        
        adjList = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                adjList[pattern].append(word)
        
        seen = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neiWord in adjList[pattern]:
                        if neiWord not in seen:
                            seen.add(neiWord)
                            q.append(neiWord)
            res += 1

        return 0


