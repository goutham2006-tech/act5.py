def combinationSum(candidates, target):
    result = []
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] <= remaining:
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()
    backtrack(0, [], target)
    return result

# Test Cases
print("Test 1:", combinationSum([2,3,6,7], 7))   # Expected: [[2,2,3],[7]]
print("Test 2:", combinationSum([2,3,5], 8))      # Expected: [[2,2,2,2],[2,3,3],[3,5]]
print("Test 3:", combinationSum([2], 1))          # Expected: []
