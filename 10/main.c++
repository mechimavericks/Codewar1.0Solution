//Back-end complete function Template for C++

class Solution {
  public:
    string isFriend(int n, int x, int y, vector<int> &arr) {
        for (auto j:arr){
            if (x+j==y) return "yes";
        }
        return "no";
    }
};
