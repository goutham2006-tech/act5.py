def subsets(nums):
    result = []
    def backtrack(start, current):
        result.append(current[:])
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    backtrack(0, [])
    return result

# Test Cases
print("Test 1:", subsets([1,2,3]))   # Expected: [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
print("Test 2:", subsets([0]))       # Expected: [[],[0]]
