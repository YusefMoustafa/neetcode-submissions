from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
    # transform beginWord to endWord
    # do this by tranforming beginWord to any word in wordList that is 1 char    different
    # keep doing this until we arrive to the endWord and return # of words we used
    # if we never arrive to the endWord return 0.

        # {'*at': ['bat', 'cat'], 'b*t': ['bat'], 'ba*': ['bat', 'bag']}

        if endWord not in wordList:
            return 0

        adjList = defaultdict(list)
        q = deque([beginWord])
        seen = set([beginWord])

        wordList.append(beginWord)

        for word in wordList:
            for char in range(len(word)):
                pattern = word[:char] + '#' + word[char+1:]
                adjList[pattern].append(word)
            
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for char in range(len(word)):
                    pattern = word[:char] + '#' + word[char+1:]
                    for nei in adjList[pattern]:
                        if nei not in seen:
                            seen.add(nei)
                            q.append(nei)
            res += 1
        return 0
        


