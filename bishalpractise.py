class solution(object):
     def climbstair(self, n):
        memo = {}
        return self.ways(n,meom)
        
        def ways(self,n,memo):
            if n in memo:
                return memo[n]

            if n == 1:
                return n
            if n == 2:
                return n

            memo[n] = self .ways(n-1, memo) + self .ways(n-2, memo)
            return memo[n]


