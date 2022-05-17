def minDistance(self, word1: str, word2: str) -> int:
        cache = [[float('inf')]*(len(word1)+1) for _ in range(len(word2)+1)]
        
        for j in range(len(word1)+1):
            cache[len(word2)][j] = len(word1) - j
        
        for i in range(len(word2)+1):
            cache[i][len(word1)] = len(word2) - i
            

            
        for i in range(len(word2)-1, -1, -1):
            for j in range(len(word1)-1, -1, -1):
                if word2[i] == word1[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                   
                    cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])
        return cache[0][0]
                