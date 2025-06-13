
class Solution {
  public:
    int firstOccurence(string &txt, string &pat) {
        if (pat[0] == '\0')
            return 0;

        // iterating over given string s to search for string x.
        for (int i = 0; txt[i] != '\0'; i++) {
            bool isMatched = true;

            // checking for string x from current index i in the string s.
            for (int j = 0; pat[j] != '\0'; j++) {
                if (txt[i + j] == 0)
                    return -1;

                // if any character doesn't match, we break the loop.
                if (txt[i + j] != pat[j]) {
                    isMatched = false;
                    break;
                }
            }

            // if string x is found, then we return the starting index.
            if (isMatched)
                return i;
        }
        // returning -1 if string x is not found.
        return -1;
    }
};

