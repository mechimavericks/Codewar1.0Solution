
class Solution
{
public:
  vector<int> findAnswer(int n, vector<int> &A)
  {
    vector<long long> pref(n, A[0]);
    for (int i = 1; i < n; i++)
    {
      pref[i] = pref[i - 1] + A[i];
    }
    stack<int> s;
    vector<int> res(n+1, 0);
    for (int i = 0; i < n; i++)
    {
      if (pref[i] > 0)
      {
        res[0] = i + 1;
        break;
      }
    }
    for (int i = n - 1; i >= 0; i--)
    {
      while (!s.empty() && pref[s.top()] <= pref[i])
        s.pop();
      if (s.empty())
        res[i+1] = 0;
      else if (i < n - 1)
        res[i + 1] = s.top() - i;

      s.push(i);
    }
    res.pop_back();
    return res;
  }
};

