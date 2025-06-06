class Solution {
  public:
    int validStrings(int n, int k, vector<string> &arr) {
        int tot=0;
        
        for (auto j:arr){
            int c=0;
            for (auto q:j){
                if (q=='a'||q=='e'||q=='i'||q=='o'||q=='u') c+=1;
            }
            if (c==k) tot+=1;
        }
        return tot;
    }
};
