'''
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
 

Example 1:

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
Example 2:

Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.
 

Constraints:

1 <= w.length <= 104
1 <= w[i] <= 105
pickIndex will be called at most 104 times.
'''



#############################
'''
Let us rephrase the problem now, given a list of offsets (i.e. prefix sums) and a target offset, 
our task is to fit the target offset into the list so that the ascending order is maintained.
'''
#############################

class Solution:

    def __init__(self, w: List[int]):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum
        

    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        target = self.total_sum * random.random()
        
        # run a linear search to find the target zone
        '''
        for i, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum:
                return i
        '''    
        
        # run a binary search to find the target zone
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()



'''
Complexity Analysis

Let NN be the length of the input list.

Time Complexity

For the constructor function, the time complexity would be \mathcal{O}(N)O(N), which is due to the construction of the prefix sums.

For the pickIndex() function, this time its time complexity would be \mathcal{O}(\log{N})O(logN), since we did a binary search on the prefix sums.

Space Complexity

For the constructor function, the space complexity remains \mathcal{O}(N)O(N), which is again due to the construction of the prefix sums.

For the pickIndex() function, its space complexity 
would be \mathcal{O}(1)O(1), since it uses constant memory. Note, here we consider the prefix sums that it operates on, as the input of the function.
'''