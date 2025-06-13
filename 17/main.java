class Solution 
{
    public static ArrayList<Integer> findAnswer(int n, int[] A) 
    {
        ArrayList<Long> pref = new ArrayList<>();
        pref.add((long) A[0]);

        // Calculate prefix sum
        for (int i = 1; i < n; i++) {
            pref.add(pref.get(i - 1) + A[i]);
        }

        Stack<Integer> s = new Stack<>();
        ArrayList<Integer> res = new ArrayList<>();
        for(int i=0;i<=n;i++)
        {
            res.add(0);
        }

        for (int i = 0; i < n; i++) {
            if (pref.get(i) > 0) 
            {
                res.set(0,i+1);
                break;
            }
        }

        for (int i = n - 1; i >= 0; i--) 
        {
            while (!s.isEmpty() && pref.get(s.peek()) <= pref.get(i)) {
                s.pop();
            }

            if (s.isEmpty()) 
            {
                res.set(i+1,0);
            } 
            else if (i < n - 1) 
            {
                res.set(i + 1, s.peek() - i);
            }

            s.push(i);
        }

        res.remove(res.size() - 1);
        return res;
    }
}
