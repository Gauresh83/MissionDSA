class Solution {
public:
    int dp[100][101];
    int n, m;

    int f(int col, int last, vector<string>& strs) {
        if (col<0) return 0;

        int& cache=dp[col][last];
        if (cache!=-1) return cache;

        // skip this column
        int ans=f(col-1, last, strs);

        // take this column 
        bool ok=(last==m) || all_of(strs.begin(), strs.end(),
            [&](const string& s) { return s[col]<=s[last];});

        if (ok)
            ans=max(ans, 1+f(col-1, col, strs));

        return cache=ans;
    }

    int minDeletionSize(vector<string>& strs) {
        n=strs.size();
        m=strs[0].size();
        memset(dp, -1, sizeof(dp));
        return m-f(m-1, m, strs);
    }
};
