nums=[3,2,4]
target = 6

for i in range(len(nums)):
    numss = target - nums[i]
    if numss in nums and i!=nums.index(numss):
        print([i, nums.index(numss)])
        # return [i , nums.index(numss)]
        break
    else:
        continue
