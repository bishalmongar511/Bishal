
def climbStairs(self, n: int) -> int:
    

    if n <= 2:
        return n
    else:
        
        step2 = 2
        current = 0
        remanning_steps = n - step2
        current = 0
        steps = climbStairs(remanning_steps)
        ways = current + steps
        return ways