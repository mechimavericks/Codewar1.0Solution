class Solution:

    def firstOccurence(self, txt, pat):
        ind_s = 0

        #iterating over given string s to search for string x.
        while ind_s < len(txt):

            if txt[ind_s] == pat[0]:
                ind_p = 0
                temp_s = ind_s

                #checking for string x from current index i in the string s.
                while temp_s < len(txt) and txt[temp_s] == pat[ind_p]:
                    ind_p += 1
                    temp_s += 1

                    #if string x is found, then we return the starting index.
                    if ind_p == len(pat):
                        return ind_s
            ind_s += 1

        #returning -1 if string x is not found.
        return -1
