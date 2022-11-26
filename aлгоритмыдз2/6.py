#6
def rob(nums):
    a = [0] * len(nums)
    a[0] = nums[0]
    a[1] = max(nums[0], nums[1])
    for i in range(2, len(a)):
        a[i] = max(a[i-1], a[i - 2] + nums[i])
    return a[-1]


list_ = [1,2,3,1]
print(max(rob(list_[1:]), rob(list_[:len(list_) - 1])))