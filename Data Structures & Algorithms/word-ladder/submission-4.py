class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        if beginWord == endWord:
            return 0

        # to avoid duplicate words
        wordList = list(set(wordList))
        if beginWord in wordList:
            wordList.remove(beginWord)

        prereq_dict = dict()

        word_queue = [(beginWord, 1, [])] 
        min_distance = None

        while word_queue:
            word, distance, past = word_queue.pop()
            
            words2 = wordList[::]
            for i in past:
                if i in words2:
                    words2.remove(i)
            
            print(f'word: {word}, distance:{distance}\nwords2:{words2}')

            diff = []
            for w2 in words2:
                count = 0
                for i,j in zip(word, w2):
                    if i!=j:
                        count+= 1
                diff.append(count)
            
            print('diff: ', diff)
            for d, w in zip(diff, words2):
                if d == 1:
                    if w == endWord:
                        if min_distance:
                            min_distance = min(min_distance, distance+1)
                        else:
                            min_distance = distance + 1
                    else:
                        word_queue.append((w, distance+1, past+[word]))
        if min_distance:
            return min_distance
        else:
            return 0
                    
                    



