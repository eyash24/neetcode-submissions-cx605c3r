import heapq

class Twitter:

    def __init__(self):
        self.time = -1
        self.heap_dict = dict()
        self.follow_dict = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.heap_dict[userId] = self.heap_dict.get(userId, []) + [(self.time, userId, tweetId)]

    def getNewsFeed(self, userId: int) -> List[int]:
        # print(self.heap_dict)
        self.time -= 1
        tweet = self.heap_dict.get(userId, [])
        max_heap = []+tweet
        follows = self.follow_dict.get(userId, None)

        if follows:
            for f in follows:
                tweets = self.heap_dict.get(f, [])
                max_heap += tweets
        
        heapq.heapify(max_heap)
        print(self.heap_dict)
        max_10 = heapq.nsmallest(10, max_heap)
        return [i[-1] for i in max_10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.time -= 1
        if followerId != followeeId:
            follows = self.follow_dict.get(followerId, [])
            if followeeId not in follows:
                self.follow_dict[followerId] = self.follow_dict.get(followerId, [])+[followeeId]
            # print('added follower:', self.follow_dict, self.heap_dict)
            

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.time -= 1
        if followeeId in self.follow_dict.get(followerId, []):
            li = self.follow_dict[followerId]
            li.remove(followeeId)
            self.follow_dict[followerId] = li    
