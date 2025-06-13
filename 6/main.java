class Solution {
    public List<Integer> valueEqualToIndex(List<Integer> nums) {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < nums.size(); i++) {
            if (nums.get(i) == i + 1) { // Adjust index to 1-based
                result.add(i + 1);      // Add to result (adjust back to 1-based)
            }
        }
        return result;
    }
}


