
class Solution {
    public static String isFriend(int n, int x, int y, int[] arr) {
        for(int e : arr)
            if(x + e == y)
                return "yes";
        return "no";
    }
}
        
