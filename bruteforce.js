// The current solution uses a Brute Force approach with a time complexity of O(n^2).
// This is because it uses two nested loops to check all possible pairs in the array.

function twoSum(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target) {
                return [i, j];
            }
        }
    }
    return null;
}

// Optimized solution using a hash map to achieve O(n) time complexity.
function twoSumOptimized(nums, target) {
    const numMap = new Map();
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (numMap.has(complement)) {
            return [numMap.get(complement), i];
        }
        numMap.set(nums[i], i);
    }
    return null;
}

// Example usage:
const nums = [2, 7, 11, 15];
const target = 9;
console.log(twoSumOptimized(nums, target)); // Output: [0, 1]