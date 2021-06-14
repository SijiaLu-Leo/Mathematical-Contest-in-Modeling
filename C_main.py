import numpy as np
from tqdm import trange
import time


# TODO: Build a binary tree
node = np.zeros(3,)
tree = []
list = []
num = 30

class Solution:
    def allPossibleFBT(self,N:int):
        ans = []

        if N == 4:
                root = []
                root.append([0,N,0])
                ans.append(root)
        left =1
        right = N-1

        while right >=5:

            right_tree = self.allPossibleFBT(N =right)
            for i in right_tree:
                root = []
                root.extend([[left,N,right]])
                root.extend(i)
                ans.append(root)
            left += 1
            right -= 1

        return ans

if __name__ == '__main__':
    start = time.time()
    a= Solution().allPossibleFBT(N=22)
    end = time.time()
    print(a[1])
    print(end-start)
    def process(a):
        ans =0 
        for i in range(len(a)):
            if i != len(a)-1:
                ans += a[i][1] + (a[i][0]+1)*a[i][0]/2
            else:
                ans += (a[i][1]+1)*a[i][1]/2
        return ans
    ans =[]
    for i in trange(len(a)):
        ans.append(process(a[i]))
    
    print(np.array(ans).min())
    print(np.array(a)[np.where(np.array(ans) == int(np.array(ans).min()))])




        


