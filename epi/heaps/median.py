import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        
        # max heap
        self.lower = []
        
        # min heap
        self.upper = []
    
    # O(1)
    def addNum(self, num: int) -> None:

        if not self.lower:
            heapq.heappush(self.lower, -num)
        elif num > -self.lower[0]:
            heapq.heappush(self.upper, num)
        else: 
            heapq.heappush(self.lower, -num)
            
        if abs(len(self.lower) - len(self.upper)) > 1:
            self.rebalance()
        

        
    
    def rebalance(self): 
        # need to redistribute from lower to upper
        if len(self.lower) > len(self.upper):
            heapq.heappush(self.upper, -heapq.heappop(self.lower))
        elif len(self.upper) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))
            
                
    
    # O(n log n)
    def findMedian(self) -> float:
        if (len(self.lower) == len(self.upper)):
            return (-self.lower[0] + self.upper[0])/2
        else:
            return -self.lower[0] if len(self.lower) > len(self.upper) else self.upper[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()