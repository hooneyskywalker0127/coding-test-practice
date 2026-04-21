def solution(nums):
    a = len(nums)//2
    set_nums = list(set(nums))
    if len(set_nums) >= a:
        return a
    else:
        return len(set_nums)