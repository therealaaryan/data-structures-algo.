We will store the number of ways a number can be decoded in a hashmap, mapping the number with its index as the keys. We'll set the len(s) key as 1 as default and iterate backwards. If the current element it 0, we'll set dp[i] = 0, else dp[i] = dp[i + 1] (its like dp[i] += dp[i + 1] if dp[i] was set 0) i.e we'll be carry-forwarding the ways. If ith element is 1 or if it is 2 (in case of 2, i+1th element must be from 0-6 to limit to 26), we'll consider two digits i.e ith and i+1th element as 1 number, and carry forwarding i + 2th element to dp[i] by doing dp[i] += dp[i + 2]. Finally, return dp[0].