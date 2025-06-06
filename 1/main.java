public class Solution 
{
    public static int validStrings(int n, int k, String[] arr) 
    {
        int totalValid = 0;

        for (String str : arr) {
            int vowelCount = 0;
            for (char ch : str.toCharArray()) {
                if ("aeiou".indexOf(ch) >= 0) {
                    vowelCount++;
                }
            }
            if (vowelCount == k) {
                totalValid++;
            }
        }

        return totalValid;
    }
}
