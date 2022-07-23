class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


        nums.sort()
        closest = sum(nums[0:3])
        for fixed in range(len(nums)-2):
            left = fixed+1
            right = len(nums)-1
            complement = target-nums[fixed]
            while left<right:
                tempSum = nums[left] + nums[right]
                currSum = nums[fixed] + tempSum
                if abs(target-currSum) < abs(target-closest):
                    closest = currSum
                if tempSum>complement:
                    right-=1
                else:
                    left+=1
                # else:
                #     out.add((nums[fixed],nums[left],nums[right]))
                #     right-=1
        return closest

    nums = [-1,2,1,-4]
    target = 1
    print(threeSumClosest(None,nums,target))