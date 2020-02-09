# coding: utf-8

from collections import defaultdict

class Solution(object):

    #  这是我的答案，超时，结果没问题
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        # 先将wordList做一个预处理
        # 将单词中的某个字母用*代替
        if beginWord not in wordList:
            wordList.append(beginWord)
        wordDict = {}
        for item in wordList:
            words = []
            for i in range(len(item)):
                words.append(item[0:i] + '*' + item[i+1:len(item)])
            wordDict[item] = words

        # 后面开始用BFS遍历
        # 注意要记录下行走过的单次轨迹，存到list中，防止死循环
        level = 1
        queue = [beginWord] # BFS队列
        nextQueue = [] # 下一个需要探索的队列，即BFS的下一层
        alreadyInDict = {}
        while queue != []:

            for keyWord in queue: # 开始扩展当前队列

                for item in wordDict[keyWord]: # item = '*ot'

                    for word in wordDict: # word = 'hog'

                        #  有匹配上的单次模式           并且没有被扩展过
                        if item in wordDict[word] and alreadyInDict.has_key(word) == False:
                            if word == endWord: # 如果就是结尾词
                                return level + 1
                            else:
                                nextQueue.append(word) # 待扩展单词入队
                                alreadyInDict[word] = 1

            level += 1
            queue = nextQueue[:]
            nextQueue = []

        return 0

    #  这是标准答案
    def ladderLength2(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        # Queue for BFS
        queue = [(beginWord, 1)]
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.pop(0)
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0


s = Solution()
print s.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"])
print s.ladderLength('a', 'c', ["a","b","c"])
print s.ladderLength("ab", "cd", ["ab","cb","cd"])
print s.ladderLength("hot","dog",["hot","cog","dog","tot","hog","hop","pot","dot"])
print s.ladderLength("hot","dog",["hot","dog","cog","pot","dot"])