class Solution {
    public boolean isSubset(int a[], int b[]) {
        int n = a.length;
        int m = b.length;
        // Create a hash map to store the frequencies of elements in array a
        HashMap<Integer, Integer> hm = new HashMap<>();

        // Increment the frequency of each element in array a
        for (int i = 0; i < n; i++) {
            hm.put(a[i], hm.getOrDefault(a[i], 0) + 1);
        }

        // Check if each element in array b is present in array a and decrement its
        // frequency
        for (int i = 0; i < m; i++) {
            if (hm.containsKey(b[i])) {
                // If frequency becomes 1, remove the element from the hash map
                if (hm.get(b[i]) == 1) {
                    hm.remove(b[i]);
                } else {
                    // Decrement the frequency of the element
                    hm.put(b[i], hm.get(b[i]) - 1);
                }
            } else {
                // If an element in array b is not present in array a, return "No"
                return false;
            }
        }

        // If all elements in array b are present in array a, return "Yes"
        return true;
    }
}

