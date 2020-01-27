# coding: utf-8

class Solution(object):
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
        alreadyIn = [beginWord] # 存一下已经探索过的单词，防止重复循环
        while queue != []:

            levelQueue = queue[:]
            for keyWord in levelQueue:
                queue.pop(0)

                for item in wordDict[keyWord]:

                    for word in wordDict:

                        if item in wordDict[word] and word not in alreadyIn:
                            if word == endWord: # 如果就是结尾词
                                if queue == []:
                                    return level + 1
                                if queue != []:
                                    return level
                            else:
                                queue.append(word) # 待扩展单词入队
                                alreadyIn.append(word)

            level += 1

        return 0


s = Solution()
# print s.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"])
# print s.ladderLength('a', 'c', ['a','b','c'])
# print s.ladderLength('ab', 'cd', ['ab','cb','cd'])
print s.ladderLength("hot","dog",["hot","cog","dog","tot","hog","hop","pot","dot"])