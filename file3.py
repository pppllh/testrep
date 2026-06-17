def two_sum(nums, target):
    """两数之和：在数组中找到两个数，使它们的和等于目标值（返回数值）"""
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return [complement, num]
        seen.add(num)
    return []


if __name__ == "__main__":
    nums = [3, 5, 2, 8, 11]
    target = 10
    result = two_sum(nums, target)
    print(f"数组: {nums}, 目标值: {target}")
    print(f"两数之和结果(数值): {result}")
