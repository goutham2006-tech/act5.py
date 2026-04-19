def permute(nums):
    result = []
    def backtrack(current, remaining):
        if not remaining:
            result.append(current[:])
            return
        for i in range(len(remaining)):
            current.append(remaining[i])
            backtrack(current, remaining[:i] + remaining[i+1:])
            current.pop()
    backtrack([], nums)
    return result

# Test Cases
print("Test 1:", permute([1,2,3]))   # Expected: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print("Test 2:", permute([0,1]))     # Expected: [[0,1],[1,0]]
print("Test 3:", permute([1]))       # Expected: [[1]]
