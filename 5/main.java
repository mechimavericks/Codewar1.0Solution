class Solution {
    // Function to locate the occurrence of the string x in the string s.
    int firstOccurence(String txt, String pat) {
        if (pat.length() == 0) {
            return 0;
        }

        // iterating over given string s to search for string x.
        for (int i = 0; i < txt.length(); i++) {
            if (i + pat.length() > txt.length()) {
                return -1;
            }

            // checking for string x from current index i in the string s.
            for (int j = 0; j < pat.length(); j++) {
                // if any character doesn't match, we break the loop.
                // if string x is found, then we return the starting index.
                if (txt.charAt(i + j) == pat.charAt(j)) {
                    if (j == (pat.length() - 1)) {
                        return i;
                    }
                } else
                    break;
            }
        }
        // returning -1 if string x is not found.
        return -1;
    }
}
